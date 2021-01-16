package DAL

import BLL.Task
import BLL.TaskLog

class TaskBase() {
    var tasks = mutableMapOf<Int, Task>()
    var logs = arrayListOf<TaskLog>()
}