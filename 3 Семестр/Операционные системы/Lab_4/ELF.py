class ELF():
    def __init__(self, ELF_file):
        self.ELF_file = ELF_file
        self.validate()
        self.header = self.parse_magick()  # ELF_HEADER
        self.e = self.header.endiannes
        self.addition_info = self.get_addition_info()
        self.shstrtab = self.get_shstrtab()
        self.sections = [self.get_section(i) for i in range(self.addition_info["e_shnum"])]
        self.symtab = self.find_symtab()
        self.strtab = self.find_strtab()
        self.symbols = [self.get_symbol(i) for i in range(int(self.symtab.sh_size / self.symtab.sh_entsize))]

    def validate(self):
        if self.ELF_file.read(4) != b'\x7fELF':
            raise Exception('File is not ELF!')

    def parse_magick(self):
        magick_number = self.ELF_file.read(16)

        _class = "ELF64" if magick_number[0] == 2 else "ELF32"  # real offset here is +4
        endianness = "little" if magick_number[1] == 1 else "big"
        version = magick_number[2]
        os_list = {
            0: "System V",
            1: "HP-UX",
            2: "NetBSD",
            3: "Linux",
            4: "GNU Hurd",
            5: "¯\\_(ツ)_/¯",
            6: "Solaris",
            7: "AIX",
            8: "IRIX",
            9: "FreeBSD",
            10: "Tru64",
            11: "Novell Modesto",
            12: "OpenBSD",
            13: "OpenVMS",
            14: "NonStop Kernel",
            15: "AROS",
            16: "Fenix OS",
            17: "CloudABI",
            18: "Stratus Technologies OpenVOS"
        }
        OS = os_list.get(magick_number[3], 0)
        ABI_version = magick_number[4]
        # unused = magick_number[5:11]
        obj_filetype_list = {
            b'\x00': "ET_NONE",
            b'\x01': "ET_REL",
            b'\x02': "ET_EXEC",
            b'\x03': "ET_DYN",
            b'\x04': "ET_CORE",
            b'\xFE\x00': "ET_LOOS",
            b'\xFE\xFF': "ET_HIOS",
            b'\xFF\x00': "ET_LOPROC",
            b'\xFF\xFF': "ET_HIPROC",
        }
        obj_filetype = obj_filetype_list.get(magick_number[12:13])
        machine_list = {
            b'\x00': "¯\\_(ツ)_/¯",
            b'\x03': "x86",
            b'\x3E': "amd64"
            # and much more
        }
        machine = machine_list.get(magick_number[14:15])
        return ELF_HEADER(_class, endianness, version, OS, ABI_version, obj_filetype, machine)

    def get_addition_info(self):
        # real offset here is +20
        additional_info = {"e_version": self.ELF_file.read(4),
                           "e_entry": int.from_bytes(self.ELF_file.read(8), self.e),
                           "e_phoff": int.from_bytes(self.ELF_file.read(8), self.e),
                           "e_shoff": int.from_bytes(self.ELF_file.read(8), self.e),
                           "e_flags": int.from_bytes(self.ELF_file.read(4), self.e),
                           "e_ehsize": int.from_bytes(self.ELF_file.read(2), self.e),
                           "e_phentsize": int.from_bytes(self.ELF_file.read(2), self.e),
                           "e_phnum": int.from_bytes(self.ELF_file.read(2), self.e),
                           "e_shentsize": int.from_bytes(self.ELF_file.read(2), self.e),
                           "e_shnum": int.from_bytes(self.ELF_file.read(2), self.e),
                           "e_shstrndx": int.from_bytes(self.ELF_file.read(2), self.e),
                           }
        return additional_info

    def get_shstrtab(self):
        sections_table_name_offset_index = self.addition_info["e_shstrndx"] * self.addition_info["e_shentsize"] + \
                                           self.addition_info["e_shoff"]
        self.ELF_file.seek(sections_table_name_offset_index, 0)
        section_with_names_bytes = self.ELF_file.read(self.addition_info["e_shentsize"])
        return ELF_SECTION(section_with_names_bytes, self)

    def get_section(self, index):
        self.ELF_file.seek(self.addition_info["e_shoff"] + index * 64)
        return ELF_SECTION(self.ELF_file.read(64), self)

    def get_string(self):
        name = ""
        while (symbol := self.ELF_file.read(1)) != b'\x00':
            name += symbol.decode("ascii")
        return name

    def print_sections(self):
        print("Idx Name \t Type \t Flags \t Address \t Offset \t Size \t Link \t Info \t Align \t EntSize")
        for (i, s) in enumerate(self.sections):
            self.ELF_file.seek(self.shstrtab.sh_offset + int.from_bytes(s.sh_name, self.e))
            print(f'[{i}] {self.get_string()}', end=' ')
            s.p()

    def find_symtab(self):
        result = None
        for section in self.sections:
            if section.sh_type == "SHT_SYMTAB":
                result = section
        if result is not None:
            return result
        raise Exception("No SYMTAB section")

    def find_strtab(self):
        result = None
        for section in self.sections:
            if section.sh_type == "SHT_STRTAB" and section.sh_name:
                if result is not None:
                    return section
                result = section
        raise Exception("No STRTAB section")

    def get_symbol(self, index):
        self.ELF_file.seek(self.symtab.sh_offset + index * self.symtab.sh_entsize)
        return ELF_SYMBOL(self.ELF_file.read(self.symtab.sh_entsize), self)

    def print_symbols(self):
        print("Idx Name \t Value \t Size \t Type \t Bind \t Visibility \t Index")
        for (i, s) in enumerate(self.symbols):
            if s.st_name is not None:
                self.ELF_file.seek(self.strtab.sh_offset + int.from_bytes(s.st_name, self.e))
                name = self.get_string()
            else:
                name = None
            print(f'[{i}] {name}', end=' ')
            s.p(self)


class ELF_HEADER():
    def __init__(self, _class, _endiannes, _version, _os, _abi, _obj_filetype, _machine):
        self._class = _class  # ELF64 or ELF32
        self.endiannes = _endiannes
        self.version = _version
        self.os = _os
        self.abi = _abi
        self.obj_filetype = _obj_filetype
        self.machine = _machine

    def __str__(self):
        fields = ["Class", "Data", "Version", "OS/ABI", "ABI version", "Type", "Machine"]
        values = [self._class, self.endiannes, self.version, self.os, self.abi, self.obj_filetype, self.machine]
        string = ""
        for i in range(len(fields)):
            string += fields[i] + ": " + str(values[i]) + '\n'
        return string


def andbytes(abytes, bbytes):
    return bytes([a & b for a, b in zip(abytes[::-1], bbytes[::-1])][::-1])


def parse_section(b, elf):
    result = []
    result.append(b[:4])  # name offset
    result.append({0: "SHT_NULL",
                   1: "SHT_PROGBITS",
                   2: "SHT_SYMTAB",
                   3: "SHT_STRTAB",
                   4: "SHT_RELA",
                   5: "SHT_HASH",
                   6: "SHT_DYNAMIC",
                   7: "SHT_NOTE",
                   8: "SHT_NOBITS",
                   9: "SHT_REL",
                   10: "SHT_SHLIB",
                   11: "SHT_DYNSYM",
                   14: "SHT_INIT_ARRAY",
                   15: "SHT_FINI_ARRAY",
                   16: "SHT_PREINIT_ARRAY",
                   17: "SHT_GROUP",
                   18: "SHT_SYMTAB_SHNDX"}.get(int.from_bytes(b[4:8], elf.e), "SHT_LOOS"))
    flags_result = []
    bf = b[8:16]
    if andbytes(bf, b'\x01\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_WRITE")
    if andbytes(bf, b'\x02\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_ALLOC")
    if andbytes(bf, b'\x04\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_EXECINSTR")
    if andbytes(bf, b'\x10\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_MERGE")
    if andbytes(bf, b'\x20\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_STRINGS")
    if andbytes(bf, b'\x40\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_INFO_LINK")
    if andbytes(bf, b'\x80\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_LINK_ORDER")
    if andbytes(bf, b'\x00\x01\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_OS_NONCONFORMING")
    if andbytes(bf, b'\x00\x02\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_GROUP")
    if andbytes(bf, b'\x00\x04\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_TLS")
    if andbytes(bf, b'\x00\x08\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_COMPRESSED")
    if andbytes(bf, b'\x0f\xf0\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_MASKOS")
    if andbytes(bf, b'\xf0\x00\x00\x00\x00\x00\x00\x00') != b'\x00\x00\x00\x00\x00\x00\x00\x00':
        flags_result.append("SHF_MASKPROC")
    result.append(flags_result)
    result.append(b[16:24])  # sh_addr
    result.append(int.from_bytes(b[24:32], elf.e))  # sh_offset
    result.append(int.from_bytes(b[32:40], elf.e))  # sh_size
    result.append(b[40:44])  # sh_link
    result.append(b[44:48])  # sh_info
    result.append(b[48:56])  # sh_addralign
    result.append(int.from_bytes(b[56:64], elf.e))  # sh_entsize
    return result


class ELF_SECTION():
    def __init__(self, bytes_array, elf):
        self.sh_name, self.sh_type, self.sh_flags, self.sh_addr, self.sh_offset, self.sh_size, self.sh_link, self.sh_info, self.sh_addralign, self.sh_entsize = parse_section(
            bytes_array, elf)

    def p(self):
        print(
            f'{self.sh_type} \t {self.sh_flags} \t {self.sh_addr} \t {self.sh_offset} \t {self.sh_size} \t {self.sh_link} \t {self.sh_info} \t {self.sh_addralign} \t {self.sh_entsize}\n')

    def __str__(self):
        fields = ["sh_name", "sh_type", "sh_flags", "sh_addr", "sh_offset", "sh_size", "sh_link", "sh_info",
                  "sh_addralign", "sh_entsize"]
        values = [self.sh_name, self.sh_type, self.sh_flags, self.sh_addr, self.sh_offset, self.sh_size, self.sh_link,
                  self.sh_info, self.sh_addralign, self.sh_entsize]
        string = ""
        for i in range(len(fields)):
            string += fields[i] + ": " + str(values[i]) + '\n'
        return string


def st_info_decode(b, elf):
    bind = {b'\x00': "STB_LOCAL",
            b'\x01': "STB_GLOBAL",
            b'\x02': "STB_WEAK",
            b'\x03': "STB_NUM",
            b'\x10': "STB_LOOS",
            b'\x11': "STB_GNU_UNIQUE",
            b'\x12': "STB_HIOS",
            b'\x13': "STB_LOPROC",
            b'\x15': "STB_HIPROC"}.get(bytes([b >> 4]))

    type = {b'\x00': "STT_NOTYPE",
            b'\x01': "STT_OBJECT",
            b'\x02': "STT_FUNC",
            b'\x03': "STT_SECTION",
            b'\x04': "STT_FILE",
            b'\x05': "STT_COMMON",
            b'\x06': "STT_TLS",
            b'\x07': "STT_NUM",
            b'\x10': "STT_LOOS",
            b'\x11': "STT_GNU_IFUNC",
            b'\x12': "STT_HIOS",
            b'\x13': "STT_LOPROC",
            b'\x15': "STT_HIPROC"}.get(bytes([b & int.from_bytes(b'\x0f', 'big')]))

    return [bind, type]


class ELF_SYMBOL():
    def __init__(self, bytes_array, elf):
        if bytes_array[:4] == b'\x00\x00\x00\x00':
            self.st_name = None
        else:
            self.st_name = bytes_array[:4]
        self.st_info = st_info_decode(bytes_array[4], elf)  # 1
        self.st_other = {b'\x00': "STV_DEFAULT",
                         b'\x01': "STV_INTERNAL",
                         b'\x02': "STV_HIDDEN",
                         b'\x03': "STV_PROTECTED"}.get(bytes([bytes_array[5]]))
        self.st_shndx = bytes_array[6:8]
        self.st_value = bytes_array[8:16]
        self.st_size = bytes_array[16:24]

    def p(self, elf):
        print(
            f'{self.st_value} \t {int.from_bytes(self.st_size, elf.e)} \t {self.st_info[1]} \t {self.st_info[0]} \t {self.st_other} \t {self.st_shndx}')
