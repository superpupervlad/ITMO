package BLL

import DAL.EmployeeBase

class EmployeeSystem(eb: EmployeeBase) {
    var employeeCounter = 0
    var employees = eb.employees
    fun newEmployeeId(): Int{
        return employeeCounter++
    }
    fun addEmployee(e: Employee){
        employees[e.id] = e
    }
    fun getEmployeeById(id: Int): Employee{
        if (id !in employees)
            throw Exception("No such employee")
        return employees[id]!!
    }
    fun getTeamLead(): TeamLead?{
        for ((key, e) in employees)
            if (e is TeamLead)
                return e
        return null
    }
}