class Deposit(client: Client, id: Int, today: CustomDate, var expireDate: CustomDate, override var interestRate: Double, money: Double = 0.0):
        Account(client, AccountTypes.DEPOSIT, id, today),
        Profitable{

    override var daysTillIncome: Int = 30
    override var currentSavings = 0.0

    fun updateTodayDate(newDate: CustomDate){
        today = newDate
    }

    override fun withdraw(amount: Int): WithdrawReply {
        return if (today < expireDate)
            WithdrawReply.BAD_WITHDRAW_BEFORE_EXPIRE_DATE
        else {
            money -= amount
            WithdrawReply.GOOD
        }
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
    }

    override fun updateDate(newDate: CustomDate){
        calculateTotalProfit(newDate)
        today = newDate
    }
}