class Client(var firstName: String,
             var lastName: String,
             var passport: String? = null,
             var address: String? = null) {
    var accounts = mutableMapOf<Int, Account>()

    fun hasAllInfo(): Boolean{
        return (passport != null && address != null)
    }

    fun newDebitAccount(accountId: Int, date: CustomDate, interestRate: Double, startMoney: Double = 0.0){
        accounts[accountId] = Debit(this, accountId, date, interestRate, startMoney)
    }

    fun newDepositAccount(accountId: Int, date: CustomDate, depositExpireDate: CustomDate, interestRate: Double, startMoney: Double = 0.0){
        accounts[accountId] = Deposit(this, accountId, date, depositExpireDate, interestRate, startMoney)
    }

    fun newCreditAccount(accountId: Int, date: CustomDate, limit: Int, commission: Double, startMoney: Double = 0.0){
        accounts[accountId] = Credit(this, accountId, date, limit, commission, startMoney)
    }

    fun updateIdentification(newPassport: String, newAddress: String){
        passport = newPassport
        address = newAddress
    }
}