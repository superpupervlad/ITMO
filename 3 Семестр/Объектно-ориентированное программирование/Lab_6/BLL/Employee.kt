package BLL

abstract class Employee(var id: Int, var name: String) {
    var boss: Employee? = null
    fun changeBoss(e: Employee) = run { boss = e }
}
enum class EmployeeTypes{
    WORKER,
    MANAGER,
    TEAMLEAD
}