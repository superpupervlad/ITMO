abstract class TransactionHandler(): IHandler<TransactionRequest> {
    protected var nextHandler: TransactionHandler? = null
    override fun setNextHandler(handler: IHandler<TransactionRequest>): TransactionHandler{
        nextHandler = handler as TransactionHandler
        return nextHandler!!
    }
}

class HasEnoughMoneyOnDebitAccount(): TransactionHandler(){
    override fun handle(handleObject: TransactionRequest): Boolean {
        return if (handleObject.senderAccount.money - handleObject.amount < 0)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleObject)
        else true
    }
}

class DontExceedLimitForSuspiciousAccount(): TransactionHandler(){
    override fun handle(handleObject: TransactionRequest): Boolean {
        return if (handleObject.senderAccount.isDoubtful() && handleObject.amount > handleObject.bankLimit)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleObject)
        else true
    }
}

