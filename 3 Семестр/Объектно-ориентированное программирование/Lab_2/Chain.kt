import java.awt.geom.PathIterator
import java.lang.Exception

class Chain {
    var shops_list = arrayListOf<Shop>()
    var scount: Int = 0
    var scodes_set: MutableSet<Int> = mutableSetOf()

    var products_list = arrayListOf<Product>()
    var pcount: Int = 0
    var pcodes_set: MutableSet<Int> = mutableSetOf()

    fun create_shop(name: String, address:String, scode: Int? = null){
        if (scode == null){
            while (scount in scodes_set){
                scount++
            }
            shops_list.add(Shop(name, address, scount))
            scodes_set.add(scount)
            scount++
        }
        else
            if (scode in scodes_set)
                throw Exception("Shop with this code already exists")
            else{
                shops_list.add(Shop(name, address, scode))
                scodes_set.add(scount)
            }
    }

    fun create_product(name: String, pcode: Int? = null): Int{
        if (pcode == null){
            while (pcount in pcodes_set){
                pcount++
            }
            products_list.add(Product(name, pcount))
            pcodes_set.add(pcount)
            pcount++
            return pcount - 1
        }
        else
            if (pcode in pcodes_set)
                throw Exception("Product with this code already exists")
            else{
                products_list.add(Product(name, pcode))
                pcodes_set.add(pcount)
                return pcode
            }
    }

    fun supply_product(scode: Int, pcode: Int, price: Int, qty: Int){
        if (pcode !in pcodes_set) throw Exception("No such product")
        if (scode !in scodes_set) throw Exception("No such shop")
        shops_list[scode].suply_product(products_list[pcode], price, qty)
    }

    fun supply_product_directly(scode: Int, name: String, price: Int, qty: Int, pcode: Int?,){
        if (scode !in scodes_set) throw Exception("No such shop")
        val actual_pcode = create_product(name, pcode)
        shops_list[scode].suply_product(products_list[actual_pcode], price, qty)
    }

    // Shop code, price
    fun find_min_price(pcode: Int, qty: Int = 1): Pair<Int, Int>?{
        var min = Int.MAX_VALUE
        var scode = 0
        for (shop in shops_list)
            if (shop.get_product_qty(pcode) >= qty && shop.get_product_price(pcode) < min) {
                min = shop.get_product_price(pcode)
                scode = shop.get_scode()
            }
        if (min == Int.MAX_VALUE) return null
        else return Pair(scode, min)
    }

    // Shop code, total
    fun find_min_price(pcode_and_qty: List<Pair<Int, Int>>): Pair<Int, Int>?{
        var min = Int.MAX_VALUE
        var scode = 0
        for (shop in shops_list) {
            var shop_total = 0
            for ((pcode, qty) in pcode_and_qty) {
                if (shop.get_product_qty(pcode) >= qty)
                    shop_total += shop.get_product_price(pcode) * qty
                else {
                    shop_total = Int.MAX_VALUE
                    break
                }
            }
            if (shop_total < min){
                scode = shop.get_scode()
                min = shop_total
            }
        }
        if (min == Int.MAX_VALUE)
            return null
        else
            return Pair(scode, min)
    }

    fun add_shop(shop: Shop, new_scode: Int? = null){
        var actual_scode = shop.get_scode()
        if (new_scode != null)
            actual_scode = new_scode
        if (actual_scode !in scodes_set){
            shops_list.add(shop)
            scodes_set.add(actual_scode)
        }
        else throw Exception("Shop with this code already in chain")
    }

    fun howMuchCanIBuy(scode: Int, money: Int): ArrayList<Triple<Product, Int, Int>>{
        return shops_list[scode].howMuchCanIBuy(money)
    }
}
