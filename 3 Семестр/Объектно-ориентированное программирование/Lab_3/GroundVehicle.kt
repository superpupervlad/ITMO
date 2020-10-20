abstract class GroundVehicle(speed: Double, val restInterval: Int, name: String = ""):
                             Vehicle(RaceType.GROUND, speed, name) {
    abstract fun restDuration(distance: Double): Double

    override fun getTime(distance: Double): Double {
        return (distance / speed) +
                restDuration(distance)
    }
}