class Backup(val title: String,
             private var content: ArrayList<Int>, // array of ids of backup files and dirs
             private val creationTime: CustomDate,
             private var directory: Directory,
             val backupId: Int,
             private val fs: Filesystem,
			 private val savingType: BackupSavingType) { // for checking files availability

	val size: Int
		get() = directory.size
	private var restorePoints = arrayListOf<RestorePoint>()
	private var restorePointCounter = 0
	private lateinit var clearRule: RPClean

	init{
		addRestorePoint(creationTime.copy(), RestorePointType.FULL)
	}

	fun checkFiles(ids: List<Int>): Boolean{
		for (id in ids)
			if (fs.findInodeById(id) == null)
				return false

		return true
	}

	private fun addAllInodes(): ArrayList<Inode>{
		val inodes = arrayListOf<Inode>()
		for (i in content){
			val inode = fs.findInodeById(i)

			if (inode == null )
				throw Exception("Can't create restore point: some files doesn't exist")
			else
				inodes.add(inode)
		}

		return inodes
	}

	private fun addOnlyChangedInodes(): ArrayList<Inode> {
		val inodes = arrayListOf<Inode>()
		for (i in content) {
			val inode = fs.findInodeById(i)

			if (inode == null)
				throw Exception("Can't create restore point: some files doesn't exist")
			else if (Pair(inode.name, inode.size) != restorePoints.last().getInodeInfo(i))
				inodes.add(inode)
		}
		return inodes
	}

	fun addRestorePoint(time: CustomDate, type: RestorePointType){
		restorePointCounter++
		val rp_directory = directory.createInode(InodeTypes.DIRECTORY, "RP#$restorePointCounter") as Directory

		if (type == RestorePointType.FULL)
			restorePoints.add(FullPoint(time.copy(), addAllInodes(), rp_directory, restorePointCounter))
		else {
			restorePoints.add(IncrementPoint(time.copy(), addOnlyChangedInodes(), rp_directory, restorePointCounter, restorePoints.last()))
			restorePoints[restorePoints.size - 2].addHeir(restorePoints.last())
		}
	}

	fun addInodes(inodes: List<Int>){
		content.addAll(inodes)
	}

	fun deleteInodes(inodes: List<Int>){
		content.removeAll(inodes)
	}

	private fun removeAllRPExcept(ids: MutableSet<Int>){
		val rp_iterator = restorePoints.iterator()
		for (rp in rp_iterator)
			if (rp.id !in ids){
				directory.deleteInode(rp.dirWithFiles.id)
				rp_iterator.remove()
			}
	}

	fun changeCleanRule(new_rule: RPClean){
		clearRule = new_rule
	}

	fun checkCleanRule():Boolean{
		return this::clearRule.isInitialized
	}

	// All 3 cleanBy functions return id's of rp that will NOT be deleted
	private fun selectByQuantity(rule: CleanByQuantity): MutableSet<Int>{
		val quantity = rule.numberOfPoints
		val savedpoints = mutableSetOf<Int>()

		for (i in restorePoints.size-1 downTo 0){
			if (savedpoints.size >= quantity || savedpoints.size == restorePoints.size)
				break
			savedpoints.addAll(restorePoints[i].getAllHeirsId())
		}

		return savedpoints
	}

	private fun selectByDate(rule: CleanByDate): MutableSet<Int>{
		val date = rule.date
		val savedpoints = mutableSetOf<Int>()

		for (i in restorePoints)
			if (i.creationDate >= date)
				savedpoints.add(i.id)

		return savedpoints
	}

	private fun selectBySize(rule: CleanBySize): MutableSet<Int>{
		val size = rule.size
		val savedpoints = mutableSetOf<Int>()
		var size_of_saved_rp = 0

		while (size_of_saved_rp < size || savedpoints.size >= restorePoints.size){
			val info = restorePoints.last().getAllHeirsIdAndTotalSize()
			savedpoints.addAll(info.first)
			size_of_saved_rp += info.second
		}

		return savedpoints
	}

	private fun hybridSelect(rule: Hybrid): MutableSet<Int>{
		val selected_rp = arrayListOf<MutableSet<Int>>()

		for (i in rule.rules)
			selected_rp.add(
				when (i){
					is CleanByQuantity -> selectByQuantity(i)
					is CleanByDate -> selectByDate(i)
					is CleanBySize -> selectBySize(i)
					else -> mutableSetOf()
				})

		return if (rule.limit == HybridLimit.ALL_LIMITS)
			selected_rp.maxByOrNull { it.size }!!
		else
			selected_rp.minByOrNull { it.size }!!
	}

	fun clean(){
		clean(clearRule)
	}

	fun clean(rule: RPClean){
		if (!checkCleanRule())
			throw Exception("Can't clean backup: rule is not set")
		val savedpoints = when (rule){
			is CleanByQuantity -> selectByQuantity(clearRule as CleanByQuantity)
			is CleanByDate -> selectByDate(clearRule as CleanByDate)
			is CleanBySize -> selectBySize(clearRule as CleanBySize)
			is Hybrid -> hybridSelect(clearRule as Hybrid)
			else -> mutableSetOf()
		}

		removeAllRPExcept(savedpoints)
	}
}