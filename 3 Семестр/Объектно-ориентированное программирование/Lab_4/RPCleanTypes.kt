class CleanByQuantity(var numberOfPoints: Int): SimpleRPClean() {

}

class CleanByDate(var date: CustomDate): SimpleRPClean(){

}

class CleanBySize(var size: Int): SimpleRPClean(){

}

class Hybrid(val rules: List<SimpleRPClean>, val limit: HybridLimit): RPClean(){

}

enum class HybridLimit(){
	ONE_LIMIT,
	ALL_LIMITS
}