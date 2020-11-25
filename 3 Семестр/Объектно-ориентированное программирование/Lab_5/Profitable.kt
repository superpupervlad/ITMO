interface Profitable {
    var interestRate: Double
    var daysTillIncome: Int
    var currentSavings: Double

    fun calculateProfitByDay(days: Int)
    fun calculateTotalProfit(newDate: CustomDate)
}