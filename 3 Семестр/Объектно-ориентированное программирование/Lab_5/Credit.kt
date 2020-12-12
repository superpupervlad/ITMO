class Credit(bank: Bank,
             client: Client,
             id: Int,
             var creditLimit: Double,
             override var interestRate: Double,
             money: Double = 0.0):
        Account(bank, client, id, money),
        Percentable {
    override var currentAccumulatedMoney: Double = 0.0

    override fun dailyUpdate() {
        if (money < 0)
            withdraw(interestRate)
    }

    override fun monthlyUpdate(): Transaction {
        /* no-op */
        return Transaction(0, bank.bs, TransactionStatusType.UNSUCCESSFUL,0.0)
    }
}