class Debit(bank: Bank,
            client: Client,
            id: Int,
            money: Double,
            override var interestRate: Double,
            override var currentAccumulatedMoney: Double):
    Account(bank, client, id, money),
    Percentable {
    override fun dailyUpdate() {
        currentAccumulatedMoney += interestRate/365/100*money
    }

    override fun monthlyUpdate(): Transaction {
        val transaction = bank.addTransaction(currentAccumulatedMoney, null, Pair(bank.id, id), TransactionStatusType.SUCCESSFUL, "Monthly update")
        money += currentAccumulatedMoney
        currentAccumulatedMoney = 0.0
        return transaction
    }
}

