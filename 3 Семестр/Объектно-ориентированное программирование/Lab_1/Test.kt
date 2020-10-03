class Test (var name: String, var age: Int){

    var height: Int = 2
        set (value) {
            field = value
        }
}


fun main(){
    println("sadk]sac".indexOfFirst { it == ']' })
    println("sadk]sac".substring(1,"sadk]sac".indexOfFirst { it == ']' }))
}