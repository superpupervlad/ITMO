class BackupSystem(private val fs: Filesystem) {

	private var backups = mutableMapOf<Int, Backup>()
	private var idCounter = 0
	private val idOfBackupsDirectory: Int = fs.addInodeToRoot(InodeTypes.DIRECTORY, "Backups")
	private var backupDirectory: Directory = fs.getDirById(idOfBackupsDirectory)!!

	// return if of backup
	fun createBackup(title: String, content:ArrayList<Int>, creationTime: CustomDate): Int{
		idCounter++
		val new_dir = backupDirectory.createInode(InodeTypes.DIRECTORY, "$title Bid:#$idCounter")
		backups[idCounter] = Backup(title,
				content,
				creationTime,
				new_dir as Directory,
				idCounter, fs)

		return idCounter
	}

	fun newRestorePoint(backup_id: Int, time: CustomDate, type: RestorePointType){
		backups[backup_id]!!.addRestorePoint(time, type)
	}

	fun changeCleanRule(backup_id: Int, rule: RPClean){
		backups[backup_id]!!.changeCleanRule(rule)
	}

	fun clean(backup_id: Int){
		backups[backup_id]!!.clean()
	}
}

enum class RestorePointType{
	FULL,
	INCREMENT
}

