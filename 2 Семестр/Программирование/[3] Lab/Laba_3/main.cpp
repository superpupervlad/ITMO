#include <iostream>
#include "Complex.h"
#include "Array.h"
#include <string.h>

void process_complex(const char **argv){
    if ((strcmp(argv[2], "--help") == 0) 
        or (strcmp(argv[2], "-h") == 0)){
        std::cout << "-x\tprint result of multiplication of 2 complex numbers\n";
        std::cout << "-p\tprint result of addition of 2 complex numbers\n";
        std::cout << "-xr\tprint result of multiplication of complex  and real numbers\n";
        std::cout << "-l, --lenght\tprint lenght of vector of complex number\n";
        std::cout << "-h, --help\tprint this menu\n";
        return;
    }
    if ((strcmp(argv[2], "--lenght") == 0) 
        or (strcmp(argv[2], "-l") == 0)){
        std::cout << "Enter real and imaginary parts of complex number\n";
        double re, im;
        std::cin >> re >> im;
        Complex c (re, im);
        std::cout << double(c) << "\n";
        return;
    }
    if ((strcmp(argv[2], "-x") == 0) or (strcmp(argv[2], "-p") == 0)){
        std::cout << "Enter real and imaginary parts of first complex number\n";
        double re1, im1, re2, im2;
        std::cin >> re1 >> im1;
        std::cout << "Enter real and imaginary parts of second complex number\n";
        std::cin >> re2 >> im2;
        Complex c1 (re1, im1);
        Complex c2 (re2, im2);

        if (strcmp(argv[2], "-x") == 0){
            print(c1 * c2);
            return;
        }
        else if (strcmp(argv[2], "-p") == 0){
            print(c1 + c2);
            return;
        }
    }
    if (strcmp(argv[2], "-xr") == 0){
        std::cout << "Enter real and imaginary parts of first complex number\n";
        double re1, im1, real;
        std::cin >> re1 >> im1;
        std::cout << "Enter real number\n";
        std::cin >> real;
        Complex c1 (re1, im1);
        print(c1 * real);
        return;
    }
    std::cout << "Syntax error!\nTry --help --complex";
}

void process_array(const char **argv){
    if ((strcmp(argv[2], "--help") == 0) 
        or (strcmp(argv[2], "-h") == 0)){
        std::cout << "-add\tprint result of concatination of 2 arrays\n";
        std::cout << "-b\tcheck if first array is bigger than second\n";
        std::cout << "-s\tcheck if first array is smaller than second\n";
        std::cout << "-e\tcheck if first array is equal second\n";
        std::cout << "-s\tcheck if first array is not equal second\n";
        std::cout << "-h, --help\tprint this menu\n";
    return;
    }
    std::cout << "Write size of arrays\n";
    int s1, s2;
    std::cin >> s1 >> s2;
    Array a1(s1);
    Array a2(s2);
    if (strcmp(argv[2], "-add") == 0){
        print(a1 + a2);
        return;
    }
    else{
        bool check = false;
        bool answer = true;
        if (strcmp(argv[2], "-b") == 0){ //bigger1
            answer = a1 > a2; check = true;}
        else if(strcmp(argv[2], "-s") == 0){ //smaller
            answer = a1 < a2; check = true;}
        else if(strcmp(argv[2], "-e") == 0){ //equal
            answer = a1 == a2; check = true;}
        else if(strcmp(argv[2], "-ne") == 0){ //equal
            answer = a1 != a2; check = true;}
        if (check == true){
            std::cout << std::boolalpha << answer << "\n";
            return;
        }
    }
    std::cout << "Syntax error!\nTry --help --array";
}

void analyze(int argc, const char **argv){
    if (((strcmp(argv[1], "--help") == 0) 
        or (strcmp(argv[1], "-h") == 0)) and (argc == 1)){
        std::cout << "-c, --complex\twork with complex numbers\n";
        std::cout << "-a, --array\twork with arrays\n";
        std::cout << "-h, --help\tshow help menu\n";
        return;
    }
    if (argc != 2){
        std::cout << "Error!\nProgram needs 2 argument, got:" << argc << "\n";
        return;
    }
    if ((strcmp(argv[1], "-c") == 0) or (strcmp(argv[1], "--complex") == 0)){
        process_complex(argv);
        return;
    }
    if ((strcmp(argv[1], "-a") == 0) or (strcmp(argv[1], "--array") == 0)){
        process_array(argv);
        return;
    }
    std::cout << "Syntax error!\nTry --help";
}

int main(int argc, const char **argv) {
    analyze(argc - 1, argv);
    return 0;
}
