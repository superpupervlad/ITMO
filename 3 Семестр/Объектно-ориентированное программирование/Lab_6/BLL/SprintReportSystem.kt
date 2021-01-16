package BLL

import DAL.SprintReportBase

class SprintReportSystem(var ts: TaskSystem, var es: EmployeeSystem, var date: CustomDate, val srb: SprintReportBase) {
    var reportDailyCounter = 0
    var reportSprintCounter = 0
    var dailyReports = srb.dailyReports
    var sprintReports = srb.sprintReports
    var finalCommandSprintReport: List<SprintReport>
        get() = srb.finalCommandSprintReport
        set(value) {srb.finalCommandSprintReport = value}
    fun newDailyReportId(): Int{
        return reportDailyCounter++
    }
    fun newSprintReportId(): Int{
        return reportSprintCounter++
    }
    fun findSprintReportByEmployeeId(id: Int): List<SprintReport>{
        var result = arrayListOf<SprintReport>()
        for ((id, report) in sprintReports)
            if (report.employee.id == id)
                result.add(report)
        return result
    }
    fun findDailyReportByEmployeeId(id: Int): List<DailyReport>{
        var result = arrayListOf<DailyReport>()
        for ((id, report) in dailyReports)
            if (report.employee.id == id)
                result.add(report)
        return result
    }
}