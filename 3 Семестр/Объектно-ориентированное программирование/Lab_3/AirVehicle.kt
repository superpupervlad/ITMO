abstract class AirVehicle(speed: Double, name: String = ""):
                          Vehicle(RaceType.AIR, speed, name) {
    abstract var distanceReducer: Double

    private fun calculateRealDistance(distance: Double): Double{
        distanceReducer = distance
        return distance - (distance/100 * distanceReducer)
    }

    override fun getTime(distance: Double): Double {
        return this.calculateRealDistance(distance) / speed
    }
}