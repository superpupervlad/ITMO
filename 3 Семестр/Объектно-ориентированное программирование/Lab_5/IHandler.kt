interface IHandler<HandleObjectType> {
    fun setNextHandler(handler: IHandler<HandleObjectType>): IHandler<HandleObjectType>
    fun handle(handleObject: HandleObjectType): Boolean
}