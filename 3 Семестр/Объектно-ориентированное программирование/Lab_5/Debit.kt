class Debit(client: Client, id: Int, today: CustomDate, override var interestRate: Double, money: Double = 0.0, ):
        Account(client, AccountTypes.DEBIT, id, today, money),
        Profitable{

    override var daysTillIncome: Int = 30
    override var currentSavings = 0.0

    override fun withdraw(amount: Int): WithdrawReply {
        return if (money - amount > 0) {
            money -= amount
            WithdrawReply.GOOD
        } else
            WithdrawReply.BAD_INSUFFICIENT_FUNDS
    }

    override fun calculateProfitByDay(days: Int){
        currentSavings += money * (interestRate / 365) * days
    }

    override fun calculateTotalProfit(newDate: CustomDate) {
        var days = newDate - today

        if (days < daysTillIncome){
            calculateProfitByDay(days)
            daysTillIncome -= days
        }
        else{
            calculateProfitByDay(daysTillIncome)
            daysTillIncome -= days
            while (daysTillIncome < 0){
                daysTillIncome += 30
                calculateProfitByDay(30)
            }
        }
        today = newDate
    }

    override fun updateDate(newDate: CustomDate) {
        calculateTotalProfit(newDate)
        today = newDate
    }
}