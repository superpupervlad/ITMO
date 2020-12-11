interface IHandler{
    var nextHandler: IHandler?
    fun setNextHandler(handler: IHandler): IHandler
    fun handle(handleBank: Bank, handleAccount: Account, amount: Double = 0.0): Boolean
}