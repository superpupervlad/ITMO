class Deposit(bank: Bank,
              client: Client,
              id: Int,
              override var interestRate: Double,
              var endDepositBlockDate: CustomDate,
              money: Double = 0.0):
        Account(bank, client, id, money),
        Percentable {
    override var currentAccumulatedMoney: Double = 0.0

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