class Data {
	private var sections: MutableMap<String, Section> = mutableMapOf()
	fun add_section(name: String){
		if (name in sections) throw Exception("Section name repeated")
		sections[name] = Section(name)
	}

	fun add_value_to_section(section: String, name: String, value: String){
		sections[section]?.add_field(name, value)
	}

	fun get_value(section: String, field_name: String, type: String): Any? {
		return when (type){
			"int" -> try{
				sections[section]?.get_value(field_name)?.toInt()
			}
			catch(e: NumberFormatException){
				throw Exception("Can't convert to this type")
			}
			"float" -> try{
				sections[section]?.get_value(field_name)?.toFloat()
			}
			catch(e: NumberFormatException){
				throw Exception("Can't convert to this type")
			}
			"string" -> sections[section]?.get_value(field_name)
			else -> throw Exception("Wrong type format")
		}
	}
}

class Section(val name: String){
	private var fields: MutableMap<String, String> = mutableMapOf()

	fun add_field(name: String, value: String){
		fields[name] = value
	}

	fun get_value(name: String): String? {
		return fields[name]
	}
}