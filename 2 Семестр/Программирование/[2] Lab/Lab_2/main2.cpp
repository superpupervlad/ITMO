#include <iostream>
#include "Complex.h"
#include <string>
#include <vector>

void analyze(int argc, std::vector<std::string> &argv){
    std::cout << argv[1] << "\n";
    if (argv[1] == "-example"){
        std::cout << "example";///////////////////////
        return;
    }
    if ((argc != 1) and (argc != 2) and (argc != 3)){
        std::cout << "Error!\nProgram needs 1, 2 or 3 argument, got:" << argc << "\n";
        return;
    }
    if ((argc == 2) and (argv[1] != "len")){
        std::cout << "Error!\nWrong syntax!\nTry -example\n";
        return;
    }
    if (argv[2] == "*"){
        Complex c1 (stod(argv[1].substr(0, argv[1].find(" "))), 1);
        c1.print();
    }

}

int main(int argc, const char **argv) {
    std::vector<std::string> v(argv,argv+argc);
    std::cout << "ARGC: " << argc;
    for (int i = 0; i < argc - 1; i++){
        std::cout << argv[i] << " ";
    }
    Complex c1(1, 0);
    analyze(argc - 1, v);
    std::cout << "a\n";
    std::cout << argv[1] << "\n";
    return 0;
}
