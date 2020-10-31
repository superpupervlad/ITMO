class BackupSystem(val fs: Filesystem) {

	var backups = mutableMapOf<Int, Backup>()
	private var idCounter = -1
	val idOfBackupsDirectory: Int = fs.addInodeToRoot(InodeTypes.DIRECTORY, "Backups")
	var backupDirectory: Directory = fs.getDirById(idOfBackupsDirectory)!!

	// return if of backup
	fun createBackup(title: String, content:List<Int>, creationTime: CustomDate): Int{
		idCounter++
		var new_dir = backupDirectory.createInode(InodeTypes.DIRECTORY, "Backup #$idCounter")
		backups[idCounter] = Backup(title, content, creationTime, new_dir as Directory, idCounter, fs)
		return idCounter
	}

	fun newRestorePoint(backup_id: Int, time: CustomDate, type: RestorePointType){
		backups[backup_id]!!.addRestorePoint(time, type)
	}
}

enum class RestorePointType{
	FULL,
	INCREMENT
}