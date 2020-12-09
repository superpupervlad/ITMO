abstract class Account(var bank: Bank,
                       val client: Client,
                       val id: Int,
                       var money: Double) {

    fun isDoubtful(): Boolean{
        return !client.isSuspicious()
    }

    fun withdraw(amount: Double){
        money -= amount
    }

    fun receive(amount: Double) {
        money += amount
    }
}