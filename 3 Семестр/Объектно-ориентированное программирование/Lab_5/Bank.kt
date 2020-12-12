class Bank(val bs: BankSystem,
           val id: Int,
           var title: String,
           var date: CustomDate,
           var limitForSuspiciousAccounts: Double,
           var depositInterestRateList: List<Pair<Double, Double>>) {
//    depositInterestRateList [(0, 1%), (100, 3%), (300, 5%), (1000, 6%) ...]
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

    fun registerNewClient(firstname: String, lastname: String, passport: String? = null, address: String? = null){
        val clientId = newClientId()
        clients[clientId] = Client(firstname, lastname, passport, address)
    }

    fun updateClientPassport(clientId: Int, newPassport: String){
        if (clientId in clients)
            clients[clientId]!!.changePassport(newPassport)
        else
            throw Exception("Can't update client info: no such client")
    }

    fun updateClientAddress(clientId: Int, newAddress: String){
        if (clientId in clients)
            clients[clientId]!!.changePassport(newAddress)
        else
            throw Exception("Can't update client info: no such client")
    }

    private fun getDepositInterestRate(money: Double): Double{
        for (range in depositInterestRateList)
            if (range.first < money)
                return range.second
        return depositInterestRateList.last().second
    }

    fun createDepositAccount(clientId: Int, depositExpireDate: CustomDate, startMoney: Double){
        if (clientId in clients) {
            val accountId = newAccountId()
            accounts[accountId] = Deposit(this, clients[clientId]!!, accountId, getDepositInterestRate(startMoney), depositExpireDate, startMoney)
        }
        else
            throw Exception("Can't create account: no such client")
    }

    fun createDebitAccount(clientId: Int, interestRate: Double){
        if (clientId in clients) {
            val accountId = newAccountId()
            accounts[accountId] = Debit(this, clients[clientId]!!, accountId, interestRate)
        }
        else
            throw Exception("Can't create account: no such client")
    }

    fun createCreditAccount(clientId: Int, interestRate: Double, creditLimit: Double){
        if (clientId in clients) {
            val accountId = newAccountId()
            accounts[accountId] = Credit(this, clients[clientId]!!, accountId, creditLimit, interestRate)
        }
        else
            throw Exception("Can't create account: no such client")
    }

    fun getDebitAccount(accountId: Int): Debit{
        return accounts[accountId] as Debit
    }

    fun getDepositAccount(accountId: Int): Deposit{
        return accounts[accountId] as Deposit
    }

    fun getCreditAccount(accountId: Int): Credit{
        return accounts[accountId] as Credit
    }

    fun addTransaction(amount: Double,
                       sendAccountId: Int?,
                       receiveAccountId: Pair<Int, Int>?,
                       status: TransactionStatusType = TransactionStatusType.PROCESSING,
                       comment: String = ""): Transaction{
        val transactionId = newTransactionId()
        if (sendAccountId == null)
            transactions[transactionId] = Transaction(transactionId, bs, status, amount, null, receiveAccountId, comment)
        else
            transactions[transactionId] = Transaction(transactionId, bs, status, amount, Pair(id, sendAccountId), receiveAccountId, comment)
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

    var debitTransferRules: TransactionHandler = HasEnoughMoneyOnAccount().
                                  setNextHandler(DontExceedLimitForSuspiciousAccount())

    var creditTransferRules: TransactionHandler = DontExceedCreditLimit().
                                   setNextHandler(DontExceedLimitForSuspiciousAccount())

    var depositTransferRules: TransactionHandler = HasEnoughMoneyOnAccount().
                                    setNextHandler(DontExceedCreditLimit().
                                    setNextHandler(CheckDepositBlockDate()))

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
            is Debit -> check = debitTransferRules.handle(this, senderAccount, amount)
            is Credit -> check = creditTransferRules.handle(this, senderAccount, amount)
            is Deposit -> check = depositTransferRules.handle(this, senderAccount, amount)
        }

        return if (check){
            newTransaction.execute()
            newTransaction
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