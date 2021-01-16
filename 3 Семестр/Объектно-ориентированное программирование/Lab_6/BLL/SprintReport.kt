package BLL

class SprintReport(id: Int, creationDate: CustomDate, employee: Employee, description: String):
    Report(id, creationDate, employee, description) {
    var reports = arrayListOf<DailyReport>()
    var status = SprintStatus.IN_WORK
}

enum class SprintStatus{
    IN_WORK,
    DONE
}