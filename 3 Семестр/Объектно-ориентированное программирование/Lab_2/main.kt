fun main() {
	val chain = Chain()
	// Creating 3 shops
	chain.create_shop("Продукты 24", "Невский пр., 1")
	chain.create_shop("Ларёк", "ул. Ленина, 42")
	chain.create_shop("ОбщОптМагСтройИнст", "ул. Без названия")
	// Create 5 products
	chain.create_product("Банан")
	chain.create_product("Компьютер")
	chain.create_product("Чипсы")
	chain.create_product("Сигареты")
	chain.create_product("Молоко")
	// Supply them
	chain.suppply_product(0, 0, 50, 10)

	chain.suppply_product(0, 1, 10000, 5)

	chain.suppply_product(0, 2, 99, 100)
	chain.suppply_product(1, 2, 100, 10)

	chain.suppply_product(0, 3, 100, 300)
	chain.suppply_product(1, 3, 150, 100)

	chain.suppply_product(0, 4, 60, 50)
	// Create and supply product directly
	chain.suppply_product_directly(1, "Газета", 110, 500)
	chain.suppply_product_directly(2, "Болты", 5, 1000)
	chain.suppply_product_directly(2, "Гайки", 3, 3000)
	chain.suppply_product_directly(2, "Лампочки", 100, 10)
	chain.suppply_product_directly(2, "Обои", 1000, 50)

	// 4 Task
	val temp_product_code = 2
	val temp_return1 = chain.find_min_price(temp_product_code)
	if (temp_return1 != null)
		println("Дешевле всего " + chain.get_product(temp_product_code)!!.name +
				" в " + chain.get_shop(temp_return1)!!.get_name() + '!')
	else
		println("В сети нет товара с таким кодом :(")

	println("\n#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#\n")

	// 5 Task
	val temp_shop_code = 0
	val temp_money = 3000
	val temp_return2 = chain.howMuchCanIBuy(temp_shop_code, temp_money)
	println("На " + temp_money +
			" в " + chain.get_shop(temp_shop_code)!!.get_name() + " вы можете купить:")
	for (triple in temp_return2){
		println(triple.second.toString() + ' ' + triple.first.name + " и тогда у вас останется " + triple.third)
	}

	println("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

	// 6 Task
	val temp_product_list = listOf(2 to 5, 3 to 10)
	val temp_total = chain.buyProducts(1, temp_product_list)
	if (temp_total != null)
		println("Общая стоимость покупки составит $temp_total")
	else
		println("В магазине недостаточно товаров")

	println("#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#")

	// 7 Task
	val temp_shop_total = chain.find_min_price(temp_product_list)
	if (temp_shop_total != null) {
		println("Дешевле всего в ${(chain.get_shop(temp_shop_total))!!.name}")
	}
	else
		println("Нет магазина с необходимым количество товаров")

	// chain.print_info()
}