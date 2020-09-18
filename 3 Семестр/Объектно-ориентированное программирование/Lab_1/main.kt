fun main(args: Array<String>){
	var parser = IniParser("test.ini")
	if (!parser.is_file_ok()){
		println("Try again!")
	}
	println(parser.get_info("SecondSection", "lastvalue", "float"))
}