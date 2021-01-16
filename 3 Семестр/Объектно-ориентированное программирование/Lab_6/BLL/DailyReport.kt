package BLL

class DailyReport(id: Int, creationDate: CustomDate, var tasks: List<Task>, employee: Employee, description: String):
    Report(id, creationDate, employee, description) {
}