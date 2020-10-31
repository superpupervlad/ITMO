class Directory(id:Int, name: String, val fs: Filesystem): Inode(id, name) {
	private var content = mutableMapOf<Int, Inode>()

	override var size: Int = 0
		get(){
			var sum = 0
			for ((_, i) in content)
				sum += i.size

			return sum
		}

	fun findIdByName(name: String): Int{
		for ((id, inode) in content)
			if (inode.name == name)
				return id

		return -1
	}

	fun findInodeById(inode_id: Int): Inode?{
		var possible_inode: Inode?
		for ((cur_id, i) in content){
			if (cur_id == inode_id)
				return i
			if (i is Directory){
				possible_inode = i.findInodeById(inode_id)
				if (possible_inode != null)
					return possible_inode
			}
		}
		return null
	}

	fun getDirById(dir_id: Int): Directory?{
		val possible_dir = findInodeById(dir_id)
		return if (possible_dir is Directory)
			possible_dir
		else
			null
	}

	fun addContent(i: Inode){
		content[i.id] = i
	}

	fun createInode(type: InodeTypes, name: String, size: Int = 0): Inode{
		val new_id = fs.newId()
		val new_inode: Inode

		if (type == InodeTypes.DIRECTORY)
			new_inode = Directory(new_id, name, fs)

		else
			new_inode = File(new_id, name, size)

		addContent(new_inode)
		return new_inode
	}

	fun createInode(i: Inode): Int{
		val new_id = fs.newId()

		if (i is Directory) {
			var d = Directory(new_id, i.name, i.fs)
			for ((_, inode) in i.content)
				d.createInode(inode)
			addContent(d)
		}
		else
			addContent(File(new_id, i.name, i.size))

		return new_id
	}

	fun check(id: Int): Boolean{
		for ((_, i) in content)
			if (i.id == id)
				return true

		return false
	}

	fun moveToDir(id: Int): Directory?{
		if (content[id] !is Directory)
			return null

		return content[id] as Directory
	}

	fun printInfo(tabs:Int = 0){
		println("\t".repeat(tabs) + name + "/ (id: $id, size: $size)")
		for ((_, i) in content)
			if (i is Directory)
				i.printInfo(tabs + 1)
			else
				println("\t".repeat(tabs + 1) + i.name + " (id: ${i.id}, size: ${i.size})")
	}
}