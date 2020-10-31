import java.lang.Exception

class RestorePoint(val creationDate: CustomDate,
                   var content: ArrayList<Inode>,
                   var dirWithFiles: Directory) {

	var idAssociation: ArrayList<Pair<Int, Int>> = arrayListOf()// real, rp

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

	fun getInodeInfo(real_id: Int): Pair<String, Int>{ // Name, size
		for (a in idAssociation)
			if (a.first == real_id){
				val inode_in_dir = dirWithFiles.findInodeById(a.second)!!
				return Pair(inode_in_dir.name, inode_in_dir.size)
			}
		throw Exception("Can't get info: no such Inode")
	}

//	fun addInode(i: Inode){
//		content.add(i)
//	}

//	fun deleteInode(i: )
}