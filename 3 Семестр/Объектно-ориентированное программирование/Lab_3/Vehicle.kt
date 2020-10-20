abstract class Vehicle(val type: RaceType, val speed: Double, val name: String = "") {
	abstract fun getTime(distance: Double): Double
}