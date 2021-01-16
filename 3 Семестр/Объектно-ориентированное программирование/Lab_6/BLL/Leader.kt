package BLL

interface Leader {
    val itself: Employee
    var subordinates: ArrayList<Employee>
    fun addSubordinate(employee: Employee){
        subordinates.add(employee)
    }
    fun printInfo(tabs: Int = 0){
        println("\t".repeat(tabs) + itself.name + " (id: ${itself.id})")
        for (e in subordinates)
            if (e is Leader)
                e.printInfo(tabs + 1)
            else
                println("\t".repeat(tabs + 1) + e.name + " (id: ${e.id}")
    }
}