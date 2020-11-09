import java.lang.Exception

class Filesystem {
	private var root = Directory(0, "Root", this)
	private var idCounter = 0
//	private var hashMap = mutableMapOf<Int, Inode>()

	fun newId(): Int{
		idCounter++
		return idCounter
	}

	fun addInodeToRoot(type: InodeTypes, name: String, size: Int = 0): Int{
		val id = newId()
		if (type == InodeTypes.DIRECTORY)
			root.addContent(Directory(id, name, this))
		else
			root.addContent(File(id, name, size))

		return id
	}

	fun addInodeToDirectory(path: List<Int>, type: InodeTypes, name: String, size: Int = 0): Int{
		var cur_dir = root

		for (dir in path)
			cur_dir = cur_dir.moveToDir(dir)!!

		val inode_id = newId()
		if (type == InodeTypes.DIRECTORY)
			cur_dir.addContent(Directory(inode_id, name, this))
		else
			cur_dir.addContent(File(inode_id, name, size))

		return inode_id
	}

	@JvmName("addInodeToDirectory1")
	fun addInodeToDirectory(path: List<String>, type: InodeTypes, name: String, size: Int = 0): Int{
		var cur_dir = root
		var next_dir: Int

		for (dir in path) {
			next_dir = cur_dir.findIdByName(dir)
			if (next_dir != -1)
				cur_dir = cur_dir.moveToDir(next_dir)!!
		}

		val inode_id = newId()
		if (type == InodeTypes.DIRECTORY)
			cur_dir.addContent(Directory(inode_id, name, this))
		else
			cur_dir.addContent(File(inode_id, name, size))

		return inode_id
	}

	fun changeSize(file_id: Int, new_size: Int){
		val possible_file = findInodeById(file_id)
		if (possible_file == null)
			throw Exception("Can't change size: wrong id")
		else
			possible_file.size = new_size
	}

	fun findInodeById(inode_id: Int): Inode?{
		return root.findInodeById(inode_id)
	}

	fun findDirWhichContainsId(id: Int): Inode?{
		return root.findDirWhichContainsId(id)
	}

	fun getDirById(dir_id: Int): Directory?{
		return root.getDirById(dir_id)
	}

	fun printInfo(){
		println("========================================")
		root.printInfo()
		println("========================================\n")
	}
}

enum class InodeTypes{
	FILE,
	DIRECTORY
}