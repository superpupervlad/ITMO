package UI

import BLL.*
class EmployeeMenu(private var es: EmployeeSystem){
    private fun askBossAdding(e: Employee){
        println("Do you want to add boss now?" +
                "1. No" +
                "2. Yes")
        if (readLine()!!.toInt() == 2)
            changeBoss(e)
    }
    private fun changeBoss(e: Employee){
        println("Enter boss' ID")
        e.changeBoss(es.getEmployeeById(readLine()!!.toInt()))
    }
    private fun askSubordinatesAdding(leader: Leader){
        var result = arrayListOf<Int>()
        println("Do you want to add subordinates employees now?" +
                "1. No" +
                "2. Yes")
        if (readLine()!!.toInt() == 2)
            addSubordinates(leader)
    }
    private fun addSubordinates(leader: Leader){
        println("Enter ids, to end type q")
        var input = readLine()!!
        while(input != "q"){
            input = readLine()!!
            leader.addSubordinate(es.getEmployeeById(input.toInt()))
        }
    }
    private fun getName(): String{
        println("Enter name of employee")
        return readLine()!!
    }
    private fun getType(): EmployeeTypes{
        while (true) {
            println(
                "Choose employee type" +
                        "1. Worker" +
                        "2. Manager" +
                        "3. TeamLead"
            )
            when (readLine()!!.toInt()){
                1 -> return EmployeeTypes.WORKER
                2 -> return EmployeeTypes.MANAGER
                3 -> return EmployeeTypes.TEAMLEAD
            }
        }
    }
    private fun handle(type: EmployeeTypes, name: String){
        when(type){
            EmployeeTypes.WORKER -> createWorker(name)
            EmployeeTypes.MANAGER -> createManager(name)
            EmployeeTypes.TEAMLEAD -> createTeamLead(name)
        }
    }
    private fun createWorker(name: String){
        val w = Worker(es.newEmployeeId(), name)
        askBossAdding(w)
        es.addEmployee(w)
    }
    private fun createManager(name: String){
        val m = Manager(es.newEmployeeId(), name)
        askBossAdding(m)
        askSubordinatesAdding(m)
        es.addEmployee(m)
    }
    private fun createTeamLead(name: String){
        val t = TeamLead(es.newEmployeeId(), name)
        askSubordinatesAdding(t)
        es.addEmployee(t)
    }
    fun addNewEmployee(){
        val name = getName()
        handle(getType(), name)
    }
    fun printEmployeesTree() {
        es.getTeamLead()?.printInfo()
    }
}