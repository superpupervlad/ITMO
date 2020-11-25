class Credit(client: Client, id: Int,  today: CustomDate, var limit: Int, var commission: Double, money: Double = 0.0):
        Account(client, AccountTypes.CREDIT, id, today, money) {
    var dayTillCommission = 30

    override fun withdraw(amount: Int): WithdrawReply {
        return if (money + limit - amount >= 0){
            money -= amount
            WithdrawReply.GOOD
        } else WithdrawReply.BAD_EXCEEDED_LIMIT
    }

    fun calculateCommission(newDate: CustomDate) {
        val days = newDate - today
        dayTillCommission -= days
        while (dayTillCommission < 0){
            money -= commission
            dayTillCommission += 30
        }
    }

    override fun updateDate(newDate: CustomDate) {
        calculateCommission(newDate)
        today = newDate
    }
}