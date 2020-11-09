class IncrementPoint(creationDate: CustomDate,
                     content: ArrayList<Inode>,
                     dirWithFiles: Directory,
                     id: Int,
                     private val originalPoint: RestorePoint): RestorePoint(creationDate, content, dirWithFiles, id){

	override fun getInodeInfo(real_id: Int): Pair<String, Int> { // Name, size
		for (a in idAssociation)
			if (a.first == real_id){
				val inode_in_dir = dirWithFiles.findInodeById(a.second)!!
				return Pair(inode_in_dir.name, inode_in_dir.size)
			}
		return if (originalPoint is FullPoint)
			originalPoint.getInodeInfo(real_id)
		else
			(originalPoint as IncrementPoint).getInodeInfo(real_id)
	}
}