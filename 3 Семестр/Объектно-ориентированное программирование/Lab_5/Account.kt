abstract class Account(var bank: Bank,
                       val client: Client,
                       val id: Int,
                       var money: Double) {

    fun isDoubtful(): Boolean{
        return !client.isSuspicious()
    }

    abstract fun withdraw(amount: Double)
    abstract fun receive(amount: Double)
}