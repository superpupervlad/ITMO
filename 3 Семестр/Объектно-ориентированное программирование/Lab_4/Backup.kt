class Backup(val title: String,
             var content: List<Int>, // array of ids of backup files and dirs
             val creationTime: CustomDate,
			 var directory: Directory,
             val backupId: Int,
             val fs: Filesystem) { // for checking files availability

	var size: Int = 0
	var restorePoints = arrayListOf<RestorePoint>()
	var restorePointCounter = -1

	init{
		addRestorePoint(creationTime, RestorePointType.FULL)
	}

	fun checkFiles(ids: List<Int>): Boolean{
		for (id in ids)
			if (fs.findInodeById(id) == null)
				return false

		return true
	}

	fun addAllInodes(): ArrayList<Inode>{
		var inodes = arrayListOf<Inode>()
		for (i in content){
			val inode = fs.findInodeById(i)
			if (inode == null )
				throw Exception("Can't create restore point: some files doesn't exist")
			else
				inodes.add(inode)
		}

		return inodes
	}

	fun addOnlyChangedInodes(): ArrayList<Inode> {
		var inodes = arrayListOf<Inode>()
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
		val rp_directory = directory.createInode(InodeTypes.DIRECTORY, "RP#$restorePointCounter")

		val inodes = if (type == RestorePointType.FULL)
			addAllInodes()
		else
			addOnlyChangedInodes()

		restorePoints.add(RestorePoint(time, inodes, rp_directory as Directory))
	}
}