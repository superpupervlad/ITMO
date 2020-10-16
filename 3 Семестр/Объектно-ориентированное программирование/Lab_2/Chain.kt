import java.awt.geom.PathIterator
import java.lang.Exception

class Chain {
    private var shops_list: MutableMap<Int, Shop> = mutableMapOf()
    private var scount: Int = 0
    // var scodes_set: MutableSet<Int> = mutableSetOf()

    private var products_list: MutableMap<Int, Product> = mutableMapOf()
    private var pcount: Int = 0

    fun create_shop(name: String, address:String): Int{
        while (scount in shops_list){
            scount++
        }
        shops_list[scount] = Shop(name, address, scount)
        scount++
        return scount - 1
    }

    fun create_product(name: String): Int{
        while (pcount in products_list){
            pcount++
        }
        products_list[pcount] = Product(name, pcount)
        pcount++
        return pcount - 1
    }

    fun suppply_product(scode: Int, pcode: Int, price: Int, qty: Int){
        if (pcode !in products_list) throw Exception("No such product")
        if (scode !in shops_list) throw Exception("No such shop")
        shops_list[scode]!!.supply_product(products_list[pcode]!!, price, qty)
    }

    fun suppply_product_directly(scode: Int, name: String, price: Int, qty: Int){
        if (scode !in shops_list) throw Exception("No such shop")
        val actual_pcode = create_product(name)
        shops_list[scode]!!.supply_product(products_list[actual_pcode]!!, price, qty)
    }

    // Shop code
    fun find_min_price(pcode: Int, qty: Int = 1): Int?{
        var min = Int.MAX_VALUE
        var scode = 0
        for ((_, shop) in shops_list)
            if (shop.get_product_qty(pcode) >= qty && shop.get_product_price(pcode) < min) {
                min = shop.get_product_price(pcode)
                scode = shop.get_scode()
            }
        if (min == Int.MAX_VALUE) return null
        else return scode
    }

    // Shop code, total
    fun find_min_price(pcode_and_qty: List<Pair<Int, Int>>): Int?{
        var min = Int.MAX_VALUE
        var scode = 0
        for ((_, shop) in shops_list) {
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
            return scode
    }

    fun add_shop(shop: Shop, new_scode: Int? = null){
        var actual_scode = shop.get_scode()
        if (new_scode != null)
            actual_scode = new_scode
        if (actual_scode !in shops_list){
            shops_list[actual_scode] = shop
        }
        else throw Exception("Shop with this code already in chain")
    }

    // Product, qty, change
    fun howMuchCanIBuy(scode: Int, money: Int): ArrayList<Triple<Product, Int, Int>>{
        if (scode in shops_list)
            return shops_list[scode]!!.howMuchCanIBuy(money)
        else
            throw Exception("No such shop")
    }

    fun print_info(){
        println("##### Общее #####" +
                "\nМагазинов: " + shops_list.size +
                "\nТоваров: " + products_list.size + "\n")
        for ((_, shop) in shops_list){
            shop.print_full_info()
        }
    }

    fun get_shop(scode: Int): Shop?{
        if (scode in shops_list)
            return shops_list[scode]
        else
            return null
    }

    fun get_product(pcode: Int): Product?{
        if (pcode in products_list)
            return products_list[pcode]
        else
            return null
    }

    fun checkShop(scode: Int): Boolean{
        return scode in shops_list
    }

    fun buyProducts(scode: Int, pcode_and_qty: List<Pair<Int, Int>>): Int?{
        if (checkShop(scode))
            return shops_list[scode]!!.buyProducts(pcode_and_qty)
        throw Exception("No such shop")
    }
}
