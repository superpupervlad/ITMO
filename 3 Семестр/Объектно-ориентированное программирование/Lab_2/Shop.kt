//package kotlin.math

class Shop(val name: String, val address: String, val scode: Int) {
    // Code, <Price, Qty>
    var assortment: MutableMap<Int, ProductInShop> = mutableMapOf()

    fun get_name(): String {return name}
    fun get_address(): String {return address}
    fun get_scode(): Int {return scode}

    fun suply_product(product: Product, price: Int, qty: Int){
        if (product.pcode !in assortment)
            assortment[product.pcode] = ProductInShop(product, price, qty)
        else {
            assortment[product.pcode]?.qty?.plus(qty)
            assortment[product.pcode]?.price = price
        }
    }

    fun suply_products(plist: List<Product>, pricelist: List<Int>, qtylist: List<Int>){
        if (plist.size != pricelist.size || pricelist.size != qtylist.size) throw Exception("Wrong lists dimension")
        for (i in plist.indices)
            suply_product(plist[i], pricelist[i], qtylist[i])
    }

    // Return name, price, qty
    fun get_product_info(pcode: Int): Triple<String, Int, Int>{
        if (pcode !in assortment) throw Exception("No product with this code")
        return Triple(assortment[pcode]!!.name, assortment[pcode]!!.price, assortment[pcode]!!.qty)
    }

    fun get_product_price(pcode: Int): Int{
        if (pcode !in assortment) throw Exception("No product with this code")
        return assortment[pcode]!!.price
    }

    fun get_product_qty(pcode: Int): Int{
        if (check_product(pcode))
            return assortment[pcode]!!.qty
        else
            return 0
    }
    fun check_product(pcode: Int): Boolean{
        return pcode in assortment && (assortment[pcode]?.qty!! > 0)
    }

    // Product, qty, change
    fun howMuchCanIBuy(money: Int): ArrayList<Triple<Product, Int, Int>>{
        var product_list: ArrayList<Triple<Product, Int, Int>> = arrayListOf<Triple<Product, Int, Int>>()
        for ((key, product) in assortment){
            val total = minOf(product.qty, money/product.price)
            product_list.add(Triple(product as Product, total, money - total*product.price))
        }
        return product_list
    }

    // <pcode, qty>
    fun buyProducts(pcode_and_qty: List<Pair<Int, Int>>): Int?{
        var total = 0
        for ((pcode, qty) in pcode_and_qty)
            if (get_product_qty(pcode) >= qty)
                total += get_product_price(pcode) * qty
            else
                return null
        for ((pcode, qty) in pcode_and_qty)
            assortment[pcode]!!.qty.minus(qty)
        return total
    }
}
