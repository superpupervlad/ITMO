package DAL

import BLL.DailyReport
import BLL.SprintReport

class SprintReportBase() {
    var dailyReports = mutableMapOf<Int, DailyReport>()
    var sprintReports = mutableMapOf<Int, SprintReport>() // draft
    lateinit var finalCommandSprintReport: List<SprintReport>
}