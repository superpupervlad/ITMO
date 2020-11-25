abstract class Account(val client: Client,
                       val type: AccountTypes,
                       val id: Int,
                       var today: CustomDate,
                       var money: Double = 0.0) {

    fun isDoubtful(): Boolean{
        return !client.hasAllInfo()
    }

    //maybe pass transaction
    fun receiveMoney(amount: Int){
        money += amount
    }

    abstract fun withdraw(amount: Int): WithdrawReply

    abstract fun updateDate(newDate: CustomDate)
}

enum class AccountTypes{
    DEBIT,
    DEPOSIT,
    CREDIT
}

enum class WithdrawReply{
    GOOD,
    BAD_INSUFFICIENT_FUNDS,
    BAD_EXCEEDED_LIMIT,
    BAD_WITHDRAW_BEFORE_EXPIRE_DATE
}