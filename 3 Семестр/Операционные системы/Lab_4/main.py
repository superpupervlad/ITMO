from ELF import *


def test1():
    elf = open("a.out", "rb")
    e = ELF(elf)
    print(e.header)
    print("========")
    e.print_sections()
    print("========")
    e.print_symbols()


if __name__ == '__main__':
    test1()
