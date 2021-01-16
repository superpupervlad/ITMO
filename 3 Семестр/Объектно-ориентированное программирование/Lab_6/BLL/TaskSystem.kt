package BLL

import DAL.TaskBase

class TaskSystem(tb: TaskBase) {
    var taskCounter = 0
    var tasks = tb.tasks
    var currentDateTime = CustomDate()
    var logs = tb.logs
    fun newTaskId(): Int{
        return taskCounter++
    }
    fun addTask(t: Task) = run { tasks[t.id] = t }
    fun findTaskById(id: Int): Task{
        if (id !in tasks)
            throw Exception("No such task")
        return tasks[id]!!
    }
    fun findTasksByCreationDate(date: CustomDate): List<Task>{
        var result = arrayListOf<Task>()
        for ((id, task) in tasks)
            if (task.creationDate == date)
                result.add(task)
        return result
    }
    fun findTasksByEditDate(date: CustomDate): List<Task>{
        var result = arrayListOf<Task>()
        for ((id, task) in tasks)
            if (task.lastEditDate == date)
                result.add(task)
        return result
    }
    fun findTasksByEmployeeId(employeeId: Int): List<Task>{
        var result = arrayListOf<Task>()
        for ((id, task) in tasks)
            if (task.employee.id == employeeId)
                result.add(task)
        return result
    }
    fun findTasksEditedByEmployee(id: Int): List<Task>{
        var result = arrayListOf<Task>()
        for (log in logs)
            if (log.user.id == id)
                tasks[log.taskId]?.let { result.add(it) }
        return result
    }
    fun findTasksInSubordinate(employee: Leader): List<Task>{
        var result = arrayListOf<Task>()
        for (sub in employee.subordinates)
            result.addAll(findTasksByEmployeeId(sub.id))
        return result
    }
    fun addComment(taskId: Int, comment: String, e: Employee){
        tasks[taskId]?.addComment(comment)
        logs.add(TaskLog(currentDateTime, taskId, comment, e))
    }
}