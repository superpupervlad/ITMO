import java.io.File

class IniParser(filepath: String) {
	private val file = File(filepath)

	// Check if file exists and its extension
	fun is_file_ok(): Boolean{
		if (!exist()) {println("File not exist"); return false}
		if (!is_ini()) {println("Wrong format"); return false}
		return true
	}
	private fun exist(): Boolean {
		return file.exists()
	}
	private fun is_ini(): Boolean{
		return file.extension == "ini"
	}

	//Get name specified type from section
	fun get_info(section: String, name: String, type: String): Any?{
		val lines: List<String> = file.readLines()

		val section_line: Int = find_section(lines, section)
		if (section_line == -1) {println("No such section"); return null}

		val name_line: Int = find_name_in_section(lines, section_line, name)
		if (name_line == -1) {println("No such name in this section"); return null}

		val value = get_value_from_line(lines, name_line)


		val wordCharPool = ('a'..'z') + ('A'..'Z') + ('0'..'9') + '_' + '.'
		if (value.any { it !in wordCharPool })
			{println("Invalid type of parameter"); return null}

		return when(type){
			"int" -> if (value.toIntOrNull() == null) {
				println("Wrong type!")
				null
			} else value.toIntOrNull()
			"float" -> if (value.toFloatOrNull() == null) {
				println("Wrong type!")
				null
			}else value.toFloatOrNull()
			"string" -> value
			else -> {println("Type misspelled!"); null}
		}
	}
	private fun find_section(lines: List<String>, section: String): Int{

		for (i in lines.indices){
			if (lines[i] != "")
				if (lines[i][0] == '[')
					if (lines[i].substring(1, lines[i].length - 1) == section)
						return i
		}
		return -1
	}
	private fun find_name_in_section(lines: List<String>, section_line: Int, correct_name: String): Int{
		var line = lines[section_line]
		var name = line
		var current_line = section_line
		while ((name != correct_name)) {
			line = lines[current_line + 1]
			if (line == "") return -1
			if (line[0] == ';') return -1
			if (current_line == lines.size) return -1

			val equal_character = line.indexOfFirst {it == '='}
			name = line.substring(0, equal_character - 1)
			current_line += 1
		}
		return current_line
	}
	private fun get_value_from_line(lines: List<String>, line_num: Int): String{
		val line = lines[line_num]
		val equal_character = line.indexOfFirst {it == '='}
		var comment_start = line.indexOfFirst { it == ';' } - 1
		if (comment_start == -2) comment_start = line.length
		return line.substring(equal_character + 2, comment_start)
	}
}