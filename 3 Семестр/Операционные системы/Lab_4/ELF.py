class ELF():
    def __init__(self, ELF_file):
        self.ELF_file = ELF_file
        self.validate()
        self.header = self.parse_magick()  # ELF_HEADER
        self.e = self.header.endiannes
        self.addition_info = self.get_addition_info()
        print(self.addition_info)

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
            b'\xFE00': "ET_LOOS",
            b'\xFEFF': "ET_HIOS",
            b'\xFF00': "ET_LOPROC",
            b'\xFFFF': "ET_HIPROC",
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
