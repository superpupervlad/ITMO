open class Product(val name: String, val pcode: Int) {

}

class ProductInShop(product: Product, var price: Int, var qty: Int): Product(product.name, product.pcode) {

}