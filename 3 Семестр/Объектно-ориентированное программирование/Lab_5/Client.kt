class Client(var firstName: String,
             var lastName: String,
             var passport: String? = null,
             var address: String? = null) {

    fun isSuspicious(): Boolean{
        return (passport == null || address == null)
    }

    fun changePassport(newPassport: String) = run { passport = newPassport }

    fun changeAddress(newAddress: String) = run { address = newAddress }
}