fun test_date(){
	println("Hello World!")
	var today = CustomDate()
	var d = CustomDate()

	today.printInfo()
	today.next()
	today.printInfo()
	today.next(430)

	if (d < today){
		println("asdjniucsddscnsdc")
	}

	today.printInfo()
}

fun test_file(){
	var fs = Filesystem()
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "RestorePoint_1")
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "RestorePoint_2")
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "RestorePoint_3")
//	fs.addInodeToDirectory(listOf("RestorePoint_1"), InodeTypes.FILE, "File")
//	fs.addInodeToDirectory(listOf("RestorePoint_2"), InodeTypes.FILE, "File")
//	fs.addInodeToDirectory(listOf("RestorePoint_3"), InodeTypes.FILE, "File")
//
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "File_Version_1")
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "File_Version_2")
//	fs.addInodeToRoot(InodeTypes.DIRECTORY, "File_Version_3")
	
	fs.printInfo()
}

fun test_bs(){
	var fs = Filesystem()
	var today = CustomDate()
	var bs = BackupSystem(fs)

	fs.addInodeToRoot(InodeTypes.DIRECTORY, "Music")
	fs.addInodeToDirectory(listOf("Music"), InodeTypes.FILE, "Rock.mp3", 5)
	fs.addInodeToDirectory(listOf("Music"), InodeTypes.FILE, "Jazz.mp3", 10)
	fs.addInodeToDirectory(listOf("Music"), InodeTypes.FILE, "Pop.mp3", 7)

	fs.addInodeToRoot(InodeTypes.DIRECTORY, "Films")
	fs.addInodeToDirectory(listOf("Films"), InodeTypes.FILE, "Drama.mp4", 50)
	fs.addInodeToDirectory(listOf("Films"), InodeTypes.FILE, "Action.mp4", 70)
	fs.addInodeToDirectory(listOf("Films"), InodeTypes.FILE, "Comedy.mp4", 40)

	fs.addInodeToRoot(InodeTypes.FILE, "system.config", 1)

		fs.printInfo()

	bs.createBackup("Multimedia backup", listOf(3, 5, 6), today)

		fs.printInfo()

	fs.changeSize(3, 1)
	fs.changeSize(5, 77)

	today.next()

	bs.newRestorePoint(0, today, RestorePointType.INCREMENT)

		fs.printInfo()
}

fun main() {
	//test_date()
	test_bs()
}