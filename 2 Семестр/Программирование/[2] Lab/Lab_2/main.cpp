#include <iostream>
#include "Complex.h"
#include <string.h>
void analyze(int argc, const char **argv){
    if (argc != 1){
        std::cout << "Error!\nProgram needs 1 argument, got:" << argc << "\n";
        return;
    }
    if ((strcmp(argv[1], "--help") == 0) 
        or (strcmp(argv[1], "-h") == 0)){
        std::cout << "-x\n\tprint result of multiplication of 2 complex numbers\n";
        std::cout << "-p\n\tprint result of addition of 2 complex numbers\n";
        std::cout << "-xr\n\tprint result of multiplication of complex  and real numbers\n";
        std::cout << "-len\n\tprint lenght of vector of complex number\n";
        std::cout << "-h, --help\n\tprint this menu\n";
        return;
    }
    if (strcmp(argv[1], "-len") == 0){
        std::cout << "Enter real and imaginary parts of complex number\n";
        double re, im;
        std::cin >> re >> im;
        Complex c (re, im);
        std::cout << c.len();
        return;
    }
    if ((strcmp(argv[1], "-x") == 0) or (strcmp(argv[1], "-p") == 0)){
        std::cout << "Enter real and imaginary parts of first complex number\n";
        double re1, im1, re2, im2;
        std::cin >> re1 >> im1;
        std::cout << "Enter real and imaginary parts of second complex number\n";
        std::cin >> re2 >> im2;
        Complex c1 (re1, im1);
        Complex c2 (re2, im2);

        if (strcmp(argv[1], "-x") == 0){
            print(c1 * c2);
            return;
        }
        else if (strcmp(argv[1], "-p") == 0){
            print(c1 + c2);
            return;
        }
    }
    if (strcmp(argv[1], "-xr") == 0){
        std::cout << "Enter real and imaginary parts of first complex number\n";
        double re1, im1, real;
        std::cin >> re1 >> im1;
        std::cout << "Enter real number\n";
        std::cin >> real;
        Complex c1 (re1, im1);
        print(c1 * real);
        return;
    }
    std::cout << "Syntax error!\nTry --help";
}

int main(int argc, const char **argv) {
    analyze(argc - 1, argv);
    return 0;
}
