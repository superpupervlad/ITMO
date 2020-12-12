class Transaction(val id: Int,
                  val bs: BankSystem,
                  var status: TransactionStatusType,
                  val amount: Double,
                  val idAccountSender: Pair<Int, Int>? = null,
                  val idAccountReceiver: Pair<Int, Int>? = null,
                  val userComment: String = "") {
    fun execute(){
        bs.accountWithdrawMoney(amount, idAccountSender)
        bs.accountReceiveMoney(amount, idAccountReceiver)
        changeStatus(TransactionStatusType.SUCCESSFUL)
    }

    fun cancel(){
        val amount = amount
        idAccountSender?.let { bs.accountReceiveMoney(amount, it) }
        idAccountReceiver?.let { bs.accountWithdrawMoney(amount, it) }

        changeStatus(TransactionStatusType.CANCELED)
    }

    fun changeStatus(newStatus: TransactionStatusType): Transaction{
        status = newStatus
        return this
    }
}

enum class TransactionStatusType{
    SUCCESSFUL,
    UNSUCCESSFUL,
    CANCELED,
    PROCESSING
}