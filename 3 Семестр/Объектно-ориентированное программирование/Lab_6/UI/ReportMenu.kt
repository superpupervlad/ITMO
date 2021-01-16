package UI

import BLL.*
class ReportMenu(var rs: SprintReportSystem) {
    fun createDailyReport(){
        println("Enter your ID")
        val e = rs.es.getEmployeeById(readLine()!!.toInt())
        println("Enter tasks IDs")
        val ids = readLine()!!.split(" ").map { it.toInt() }
        var tasks = arrayListOf<Task>()
        for (id in ids)
            tasks.add(rs.ts.findTaskById(id))
        println("Enter report description")
        val desc = readLine()!!
        val id = rs.newDailyReportId()
        rs.dailyReports[id] = DailyReport(id, rs.date, tasks, e, desc)
    }
    fun createSprintReport(){
        println("Enter your ID")
        val e = rs.es.getEmployeeById(readLine()!!.toInt())
        if (e is Leader)
            askToShowSubordinatesReports(e)
        askToShowDailyReports(e.id)
        println("Enter report description")
        val desc = readLine()!!
        val id = rs.newSprintReportId()
        val sr = SprintReport(id, rs.date, e, desc)
        rs.sprintReports[id] = sr
    }
    fun askToShowDailyReports(eId: Int){
        println("Do you want to see your daily reports?" +
                "1. Yes" +
                "2. No")
        if (readLine()!!.toInt() == 1)
            printDailyReport(rs.findDailyReportByEmployeeId(eId))
    }
    fun askToShowSubordinatesReports(l: Leader){
        println("Do you want to see reports of subordinates?" +
                "1. Yes" +
                "2. No")
        if (readLine()!!.toInt() == 1)
            for (e in l.subordinates)
                printSprintReport(rs.findSprintReportByEmployeeId(e.id))
    }
    fun printSprintReport(r: SprintReport){
        println("Description: ${r.description}")
        println("Total daily reports: ${r.reports.size}")
        for (dr in r.reports)
            printDailyReport(dr)
    }
    fun printSprintReport(rs: List<SprintReport>){
        for (r in rs)
            printSprintReport(r)
    }
    fun printDailyReport(r: DailyReport){
        println("Description: ${r.description}")
        println("ID: ${r.id}")
    }
    fun printDailyReport(rs: List<DailyReport>){
        for (r in rs)
            printDailyReport(r)
    }
    fun createCommandReport(){
        val result = arrayListOf<SprintReport>()
        for ((id, r) in rs.sprintReports)
            result.add(r)
        rs.finalCommandSprintReport = result
    }
}