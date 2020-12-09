class Transaction(val id: Int,
                  var status: TransactionStatusType,
                  val amount: Double,
                  val idAccountSender: Pair<Int, Int>? = null,
                  val idAccountReceiver: Pair<Int, Int>? = null,
                  val userComment: String = "") {

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