import java.time.LocalDate
import java.time.temporal.ChronoUnit

class CustomDate(year: Int = 2000, month: Int = 10, day: Int = 1) {
    private var date = LocalDate.of(year, month, day)

    fun next(days: Long = 1){
        date = date.plusDays(days)
    }

    fun printInfo(){
        println("Date is $date")
    }

    operator fun compareTo(other: CustomDate): Int {
        return if (date.isBefore(other.date))
            -1
        else
            1
    }

    operator fun minus(other: CustomDate): Int{
        return ChronoUnit.DAYS.between(date, other.date).toInt()
    }

    fun copy(year: Int = this.date.year, month: Int = this.date.monthValue, day: Int = this.date.dayOfMonth) = CustomDate(year, month, day)
}