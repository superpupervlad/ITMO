import kotlin.experimental.and

class Race(val type: RaceType, val distance: Double) {
    var playerList: ArrayList<Vehicle> = arrayListOf()

    fun addPlayer(player: Vehicle){
        if (player.type.value and type.value != 0x00.toByte())
            playerList.add(player)
        else
            throw Exception("Vehicle can't join race: wrong type")
    }

    fun addPlayer(players: List<Vehicle>){
        for (p in players)
            addPlayer(p)
    }

    fun start(): Vehicle{
        if (playerList.size < 0)
            throw Exception("Can't start race: zero players")
        var fastest = Pair(playerList[0].getTime(distance), playerList[0])
        for (v in playerList){
            if (v.getTime(distance) < fastest.first){
                fastest = Pair(v.getTime(distance), v)
            }
        }
        return fastest.second
    }

    fun simulate(){
        //var playerTime: ArrayList<Vehicle> = arrayListOf()
        println("Total players: ${playerList.size}")
        for (v in playerList){
            println("${v.name} - ${v.getTime(distance)}")
        }
    }
}

enum class RaceType(bitField: Byte) {
    GROUND(0x01), AIR(0x02),
    ALL(0x0F);
    val value: Byte = bitField
}