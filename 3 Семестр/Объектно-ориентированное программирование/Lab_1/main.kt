fun main(args: Array<String>) {
	var parser = IniParser("test.ini")
	if (!parser.is_file_ok()) {
		throw Exception("Problem with file!")
	} else println(1) //println(parser.get_info<Int>("SecondSection", "lastvalue", "float"))
	val d = parser.parse()
	print(d.get_value("SecondSection", "sstring", "string"))
}