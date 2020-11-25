class Transaction(val id: Int,
                  val amount: Int,
                  val idAccountSender: Int,
                  val idAccountReceiver: Int,
                  var status: TransactionStatusType,
                  val comment: String = "") {

    fun cancel(){
        status = TransactionStatusType.CANCELED
    }
}

enum class TransactionStatusType{
    SUCCESSFUL,
    UNSUCCESSFUL,
    CANCELED,
    PROCESSING
}