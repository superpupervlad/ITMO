class BankSystem() {
    var banks = mutableMapOf<Int, Bank>()
    var bankIdCounter = 0

    var transactions = mutableMapOf<Int, Transaction>()
    private var transactionIdCounter = 0

    fun newTransactionId(): Int{
        return transactionIdCounter++
    }

    private fun newBankId(): Int{
        return bankIdCounter++
    }

    fun createBank(title: String, date: CustomDate, limitForSuspiciousAccounts: Double, depositInterestRateList: List<Pair<Double, Double>>){
        val bankId = newBankId()
        banks[bankId] = Bank(this, bankId, title, date, limitForSuspiciousAccounts, depositInterestRateList)
    }

    fun getBank(bankId: Int): Bank{
        if (bankId in banks)
            return banks[bankId]!!
        else throw Exception("Can't find bank")
    }

    fun checkAccount(bankId: Int, accountId: Int): Boolean{
        return banks[bankId]?.checkAccount(accountId) ?: return false
    }

    fun checkAccount(info: Pair<Int, Int>): Boolean{
        return checkAccount(info.first, info.second)
    }

    fun accountReceiveMoney(amount: Double, bankAccountId: Pair<Int, Int>?){
        if (bankAccountId != null) {
            banks[bankAccountId.first]?.accountReceiveMoney(amount, bankAccountId.second)
        }
    }

    fun accountWithdrawMoney(amount: Double, bankAccountId: Pair<Int, Int>?){
        if (bankAccountId != null) {
            banks[bankAccountId.first]?.accountWithdrawMoney(amount, bankAccountId.second)
        }
    }

    fun cancelTransaction(transactionId: Int){
        if (transactionId !in transactions)
            throw Exception("Can't cancel transaction: No such transaction")
        transactions[transactionId]!!.cancel()
    }
}