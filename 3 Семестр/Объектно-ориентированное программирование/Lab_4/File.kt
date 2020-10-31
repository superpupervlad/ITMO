class File(id:Int, name: String, override var size: Int): Inode(id, name) {
//	val name: String
//		get() {
//			val check = filepath.lastIndexOf('/')
//			return if (check == -1)
//				filepath.substring(filepath.lastIndexOf('\\') + 1)
//			else
//				filepath.substring(check + 1)
//		}
}