class Archive(id:Int,
              name: String,
              fs: Filesystem,
              var files: List<Inode>): Directory(id,
												 name,
												 fs){
	fun extract(destination: Directory){
		for (f in files)
			destination.addContent(f)
	}
}