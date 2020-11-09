abstract class RestorePoint(val creationDate: CustomDate,
                            private var content: ArrayList<Inode>,
                            var dirWithFiles: Directory,
                            val id: Int) {

	var idAssociation: ArrayList<Pair<Int, Int>> = arrayListOf()// real, rp
	private lateinit var heir: RestorePoint

	init {
		for (i in content)
			idAssociation.add(Pair(i.id, dirWithFiles.createInode(i)))
	}

	val size:Int
		get(){
			var sum = 0
			for (f in content)
				sum += f.size
			return sum
		}

	abstract fun getInodeInfo(real_id: Int): Pair<String, Int>

	fun hasHeir(): Boolean{
		return this::heir.isInitialized
	}

	fun addHeir(h: RestorePoint){
		heir = h
	}

	fun getAllHeirsId(): List<Int>{
		val heirs = arrayListOf(id)

		if (hasHeir())
			heirs.addAll(heir.getAllHeirsId())

		return heirs
	}

	fun getAllHeirsIdAndTotalSize(): Pair<ArrayList<Int>, Int>{
		val heirsAndSize: Pair<ArrayList<Int>, Int> = Pair(arrayListOf(id), size)

		if (hasHeir()) {
			val info = heir.getAllHeirsIdAndTotalSize()
			heirsAndSize.first.addAll(info.first)
			heirsAndSize.second + info.second
		}

		return heirsAndSize
	}
}