package BLL

class Manager(id: Int, name: String): Employee(id, name), Leader {
    override val itself = this
    override var subordinates = arrayListOf<Employee>()
}