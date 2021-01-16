package BLL

class Task(var ts: TaskSystem, val id: Int, var creationDate: CustomDate, var name: String, var description: String, var employee: Employee) {
    var lastEditDate = creationDate
    var status = TaskStatus.OPEN
    lateinit var comments: ArrayList<String>

    fun addComment(comment: String){
        comments.add(comment)
    }
}

enum class TaskStatus{
    OPEN,
    ACTIVE,
    RESOLVED
}