import java.util.Arrays.asList

fun main(){
    val ct = CamelTwo()
    val cf = CamelFast()
    val c  = Centaur()
    val fs = FastShoes()

    val cp = CarpetPlane()
    val m  = Mortar()
    val b = Broom()

    val gr = Race(RaceType.GROUND, 5000.0)
    gr.addPlayer(asList(ct, cf, c, fs))
    gr.simulate()
    println("Winner is ${gr.start().name}\n")

    val ar = Race(RaceType.AIR, 3000.0)
    ar.addPlayer(asList(cp, m, b))
    ar.simulate()
    println("Winner is ${ar.start().name}\n")

    val multirace = Race(RaceType.ALL, distance = 10000.0)
    multirace.addPlayer(asList(ct, cf, c, fs, cp, m, b))
    multirace.simulate()
    println("Winner is ${multirace.start().name}\n")
}