class Bank(val bs: BankSystem, val id: Int, var title: String, var date: CustomDate, var limitForSuspiciousAccounts: Double) {

    var accounts = mutableMapOf<Int, Account>()
    private var accountIdCounter = 0

    var clients = mutableMapOf<Int, Client>()
    private var clientIdCounter = 0

    var transactions = bs.transactions

    private fun newAccountId(): Int{
        return accountIdCounter++
    }

    private fun newClientId(): Int{
        return clientIdCounter++
    }

    private fun newTransactionId(): Int{
        return bs.newTransactionId()
    }

    fun checkAccount(accountId: Int): Boolean{
        return accountId in accounts
    }

    fun accountReceiveMoney(amount: Double, accountId: Int){
        accounts[accountId]?.receive(amount)
    }

    fun accountWithdrawMoney(amount: Double, accountId: Int){
        accounts[accountId]?.withdraw(amount)
    }

    fun addTransaction(amount: Double,
                       sendAccountId: Int?,
                       receiveAccountId: Pair<Int, Int>?,
                       status: TransactionStatusType = TransactionStatusType.PROCESSING,
                       comment: String = ""): Transaction{
        val transactionId = newTransactionId()
        if (sendAccountId == null)
            transactions[transactionId] = Transaction(transactionId, status, amount, null, receiveAccountId, comment)
        else
            transactions[transactionId] = Transaction(transactionId, status, amount, Pair(id, sendAccountId), receiveAccountId, comment)
        return transactions[transactionId]!!
    }

    fun cancelTransaction(transactionId: Int){
        bs.cancelTransaction(transactionId)
    }

    fun nextDay(){
        date++
        if (date.date.dayOfMonth == 1)
            for ((_, acc) in accounts)
                if (acc is Percentable) {
                    acc.dailyUpdate()
                    acc.monthlyUpdate()
                }
        else
            for ((_, acc) in accounts)
                if (acc is Percentable)
                    acc.dailyUpdate()
    }

    var debitTransferRules: TransactionHandler = HasEnoughMoneyOnDebitAccount().
                                  setNextHandler(DontExceedLimitForSuspiciousAccount())

    fun sendMoney(amount: Double, senderAccountId: Int, receiverAccountId: Pair<Int, Int>? = null, userComment: String = ""): Transaction{
        if (senderAccountId !in accounts)
            throw Exception("Sender account does not exist in this bank")
        if (receiverAccountId != null && bs.checkAccount(receiverAccountId))
            throw Exception("Receiver account does not exist in this bank")
        val senderAccount = accounts[senderAccountId]!!

        val newTransaction = addTransaction(amount,
                                            senderAccountId,
                                            receiverAccountId,
                                            TransactionStatusType.PROCESSING,
                                            userComment)

        var check = false
        when(senderAccount){
            is Debit -> check = debitTransferRules.handle(TransactionRequest(amount, senderAccount))
        }

        return if (check){
            senderAccount.withdraw(amount)
            if (receiverAccountId != null)
                bs.accountReceiveMoney(amount, receiverAccountId)
            newTransaction.changeStatus(TransactionStatusType.SUCCESSFUL)
        }
        else
            newTransaction.changeStatus(TransactionStatusType.UNSUCCESSFUL)
    }

    fun depositMoney(amount: Double, accountId: Int, userComment: String = ""): Transaction{
        if (accountId !in accounts) throw Exception("Account does not exist in this bank")

        accounts[accountId]!!.receive(amount)
        return addTransaction(amount, null, Pair(id, accountId), TransactionStatusType.SUCCESSFUL, userComment)
    }
}