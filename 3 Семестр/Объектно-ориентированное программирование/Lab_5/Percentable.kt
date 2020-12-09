interface Percentable {
    var interestRate: Double
    var currentAccumulatedMoney: Double
    fun dailyUpdate()
    fun monthlyUpdate(): Transaction
}