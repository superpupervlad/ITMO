import kotlin.math.floor

class CamelTwo: GroundVehicle(10.0, 30, "Двугорбый верблюд"){
    override fun restDuration(distance: Double): Double{
        val time = distance / speed
        when{
            time > restInterval -> return 5.0 +
                    8.0*(floor(time/restInterval) - 1)
            else -> return 0.0
        }
    }
}

class CamelFast: GroundVehicle(40.0, 10, "Верблюд-быстроход"){
    override fun restDuration(distance: Double): Double{
        val time = distance / speed
        when{
            time > 3*restInterval -> return 11.5 +
                    floor(time/restInterval) * 8
            time > 2*restInterval -> return 11.5
            time > restInterval -> return 5.0
            else -> return 0.0
        }
    }
}

class Centaur: GroundVehicle(15.0, 8, "Кентавр"){
    override fun restDuration(distance: Double) = floor(distance/speed/restInterval)* 2.0
}

class FastShoes: GroundVehicle(6.0, 60, "Сапоги-быстроходы"){
    override fun restDuration(distance: Double): Double{
        val time = distance / speed
        when{
            time > restInterval -> return 10.0 +
                    5.0*floor(time/restInterval)
            else -> return 0.0
        }
    }
}

class CarpetPlane: AirVehicle(10.0, "Ковер-самолет"){
    override var distanceReducer: Double = 0.0
        get() = field
        set(value) {
            field = when(value) {
                in 0.0..999.0 -> 0.0
                in 0.0..4999.0 -> 3.0
                in 0.0..9999.0 -> 10.0
                else -> 5.0
            }
        }
}

class Mortar: AirVehicle(8.0, "Ступа"){
    override var distanceReducer: Double = 0.0
        get() = 6.0
}

class Broom: AirVehicle(20.0, "Метла"){
    override var distanceReducer: Double = 0.0
        get() = field
        set(value) {
            if (value <= 1000)
                field = 0.0
            else
                field = (floor(value/1000) + 1) * 0.5
        }
}