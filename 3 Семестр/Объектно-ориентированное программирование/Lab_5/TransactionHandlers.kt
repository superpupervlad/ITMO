abstract class TransactionHandler(): IHandler{
    override var nextHandler: IHandler? = null
    override fun setNextHandler(handler: IHandler): TransactionHandler {
        nextHandler = handler as TransactionHandler
        return nextHandler as TransactionHandler
    }

}

class HasEnoughMoneyOnAccount(): TransactionHandler(){
    override fun handle(handleBank: Bank, handleAccount: Account, amount: Double): Boolean {
        return if (handleAccount.money - amount < 0)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleBank, handleAccount, amount)
        else true
    }
}

class DontExceedLimitForSuspiciousAccount(): TransactionHandler(){
    override fun handle(handleBank: Bank, handleAccount: Account, amount: Double): Boolean {
        return if (handleAccount.isDoubtful() && amount > handleBank.limitForSuspiciousAccounts)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleBank, handleAccount, amount)
        else true
    }
}

class DontExceedCreditLimit(): TransactionHandler(){
    override fun handle(handleBank: Bank, handleAccount: Account, amount: Double): Boolean {
        return if (handleAccount.money - amount < handleBank.getCreditAccount(handleAccount.id).creditLimit)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleBank, handleAccount, amount)
        else true
    }
}

class CheckDepositBlockDate(): TransactionHandler(){
    override fun handle(handleBank: Bank, handleAccount: Account, amount: Double): Boolean {
        return if (handleBank.date < handleBank.getDepositAccount(handleAccount.id).endDepositBlockDate)
            false
        else if (nextHandler != null)
            nextHandler!!.handle(handleBank, handleAccount, amount)
        else true
    }
}


