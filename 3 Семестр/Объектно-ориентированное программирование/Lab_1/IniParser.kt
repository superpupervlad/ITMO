import java.io.File
import java.util.*

class IniParser(filepath: String) {
	private val file = File(filepath)
	private var sections: Data = Data()

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

	private fun is_word(s: String): Boolean {
		return s.matches(Regex("\\w+"))
	}

	fun parse(): Data{
		val scanner = Scanner(file)
		var current_section: String = ""
		while(scanner.hasNext()){
			var current_line = scanner.nextLine()
			if (current_line == "" || current_line[0] == ';') continue
			if (current_line[0] == '[') {
				current_section = add_sec(current_line)
				if (scanner.hasNext()) current_line = scanner.nextLine() else break

				while (current_line != ""){
					if (current_line[0] == ';') { current_line = scanner.nextLine(); continue }
					add_field(current_line, current_section)
					if (scanner.hasNext()) current_line = scanner.nextLine() else break
				}
			}
			else throw Exception("Wrong syntax in file")
			// current_line = scanner.nextLine()
			// if (current_line == "") throw Exception("Wrong syntax in file")
		}
		return sections
	}

	private fun add_field(line: String, current_section: String){
		val uncomment_line = line.split(';')[0]
		if (uncomment_line.matches(Regex("\\w+\\s*=\\s*([\\w\\.]*|[+-]?\\d*\\.?\\d*)+\\s*"))) {
			val uncomment_line_split = uncomment_line.split('=')
			sections.add_value_to_section(current_section, uncomment_line_split[0].trim(), uncomment_line_split[1].trim())
		}
		else
			throw Exception("Wrong syntax in file: broken field")
	}

	private fun add_sec(line: String): String{
		val uncomment_line = line.split(';')[0]
		if (!uncomment_line.matches(Regex("\\[\\w+\\]\\s*")))
			throw Exception("Wrong syntax in file: broken section")
		val close_bracket_pos = uncomment_line.indexOfFirst { it == ']' }
		val section_name: String
		if (close_bracket_pos != -1)
			section_name = uncomment_line.substring(1, close_bracket_pos).trim()
		else
			throw Exception("Wrong syntax in file: broken section")
		if (!section_name.matches(Regex("\\w+"))) throw Exception("Wrong syntax in file")
		sections.add_section(section_name)
		return section_name
	}
}