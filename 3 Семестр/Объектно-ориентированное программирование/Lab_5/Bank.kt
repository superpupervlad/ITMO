class Bank(val id: Int, var title: String, var limitForSuspiciousAccounts: Int) {
    var accounts = mutableMapOf<Int, Account>()
    private var accountIdCounter = 0

    var clients = mutableMapOf<Int, Client>()
    private var clientIdCounter = 0

    var transactions = mutableMapOf<Int, Transaction>()
    private var transactionIdCounter = 0

    init {
        clients[-1] = Client("Bank", "Account")
    }

    private fun newAccountId(): Int{
        return accountIdCounter++
    }

    private fun newClientId(): Int{
        return clientIdCounter++
    }

    private fun newTransactionId(): Int{
        return clientIdCounter++
    }

    fun registerNewClient(firstname: String, lastname: String, passport: String? = null, address: String? = null){
        val clientId = newClientId()
        clients[clientId] = Client(firstname, lastname, passport, address)
    }

    fun identifiedClient(clientId:Int, passport: String, address: String){
        if (clientId in clients)
            clients[clientId]!!.updateIdentification(passport, address)
        else
            throw Exception("Can't identified client: No such client")
    }

    fun newDebitAccount(clientId: Int, date: CustomDate, interestRate: Double, startMoney: Double = 0.0){
        if (clientId in clients)
            clients[clientId]!!.newDebitAccount(newAccountId(), date, interestRate, startMoney)
        else
            throw Exception("Can't create account: no such account")
    }

    fun newDepositAccount(clientId: Int, date: CustomDate, depositExpireDate: CustomDate, interestRate: Double, startMoney: Double = 0.0){
        if (clientId in clients)
            clients[clientId]!!.newDepositAccount(newAccountId(), date, depositExpireDate, interestRate, startMoney)
        else
            throw Exception("Can't create account: no such account")
    }

    fun newCreditAccount(clientId: Int, date: CustomDate, limit: Int, commission: Double, startMoney: Double = 0.0){
        if (clientId in clients)
            clients[clientId]!!.newCreditAccount(newAccountId(), date, limit, commission, startMoney)
        else
            throw Exception("Can't create account: no such account")
    }

    private fun addTransaction(amount: Int,
                               sendAccountId: Int,
                               receiveAccountId: Int,
                               status: TransactionStatusType,
                               comment: String = ""): Transaction{
        val transactionId = newTransactionId()
        transactions[transactionId] = Transaction(transactionId, amount, sendAccountId, receiveAccountId, status, comment)
        return transactions[transactionId]!!
    }

    fun sendMoney(sendAccountId: Int, receiveAccountId: Int, amount: Int): Transaction{
        var comment = "Can't send money: "
        if (sendAccountId !in accounts) throw Exception(comment + "Sender account does not exist in this bank")
        if (receiveAccountId !in accounts) throw Exception(comment + "Receiver account does not exist in this bank")

        if (accounts[sendAccountId]!!.isDoubtful() && amount > limitForSuspiciousAccounts){
            return addTransaction(amount,
                                  sendAccountId,
                                  receiveAccountId,
                                  TransactionStatusType.UNSUCCESSFUL,
                          comment + "Amount of money is too big for suspicious account")
        }

        comment += when(accounts[sendAccountId]!!.withdraw(amount)){
            WithdrawReply.BAD_INSUFFICIENT_FUNDS -> "Not enough money on account"
            WithdrawReply.BAD_EXCEEDED_LIMIT -> "Credit limit is exceeded"
            WithdrawReply.BAD_WITHDRAW_BEFORE_EXPIRE_DATE -> "Expire date is not come yet"
            WithdrawReply.GOOD -> {
                accounts[receiveAccountId]!!.receiveMoney(amount)
                return addTransaction(amount,
                        sendAccountId,
                        receiveAccountId,
                        TransactionStatusType.SUCCESSFUL)
            }
        }

        return addTransaction(amount,
                              sendAccountId,
                              receiveAccountId,
                              TransactionStatusType.UNSUCCESSFUL,
                              comment)
    }

    fun withdrawMoney(accountId: Int, amount: Int){
        sendMoney(accountId, -1, amount)
    }

    fun cancelTransaction(transactionId: Int){
        if (transactionId !in transactions) throw Exception("Can't cancel transaction: No such transaction")

        transactions[transactionId]!!.cancel()
    }
}