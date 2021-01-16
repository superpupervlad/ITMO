package UI

import BLL.CustomDate
import BLL.EmployeeSystem
import BLL.Task
import BLL.TaskSystem
class TaskMenu(val ts: TaskSystem, val es: EmployeeSystem, var date: CustomDate) {
    fun addTask(){
        println("Enter task name")
        val name = readLine()!!
        println("Enter task description")
        val description = readLine()!!
        println("Enter employee ID")
        val employeeId = readLine()!!.toInt()
        val t = Task(ts, ts.newTaskId(), date, name, description, es.getEmployeeById(employeeId))
        ts.addTask(t)
    }
    fun printTask(t: Task){
        println("ID: $t.id")
        println("Name: ${t.name}")
        println("Description: ${t.description}")
        println("Employee ID: ${t.employee}")
        println("Comments: ${t.comments}")
    }
    fun printTask(ts: List<Task>){
        for (t in ts)
            printTask(t)
    }
    fun findTask(){
        println("Find task by: " +
                "1. ID" +
                "2. Creation date" +
                "3. Last edit date" +
                "4. Employee" +
                "5. Employee that edit it" +
                "6. Leader's subordinates")
        when (readLine()!!.toInt()){
            1 -> {
                println("Enter task ID")
                printTask(ts.findTaskById(readLine()!!.toInt()))}
            2 -> {
                println("Enter creation date in yyy-mm-dd format")
                printTask(ts.findTasksByCreationDate(CustomDate(readLine()!!)))}
            3 -> {
                println("Enter edit date in yyy-mm-dd format")
                printTask(ts.findTasksByEditDate(CustomDate(readLine()!!)))}
            4 -> {
                println("Enter employee ID")
                printTask(ts.findTasksByEmployeeId(readLine()!!.toInt()))}
            5 -> {
                println("Enter employee ID")
                printTask(ts.findTasksEditedByEmployee(readLine()!!.toInt()))}
            6 -> {
                println("Enter leader's ID")
                printTask(ts.findTasksEditedByEmployee(readLine()!!.toInt()))}
        }
    }
    fun addComment(){
        println("Enter employee ID")
        val e = es.getEmployeeById(readLine()!!.toInt())
        println("Enter task ID")
        val id = readLine()!!.toInt()
        println("Enter comment")
        val comment = readLine()!!
        ts.addComment(id, comment, e)
    }
}