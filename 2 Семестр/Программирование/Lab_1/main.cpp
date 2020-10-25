#include "functions.h" 
#include <iostream>

void task1(){
    std::cout << "Task 1" << std::endl;
    int a = 123, b = 987;
    change_biggest(a, b);
    std::cout << "Preference:" << a << b << std::endl;
    a = 123, b = 987;
    change_biggest(&a, &b);
    std::cout << "Pointers:" << a << b << std::endl;
}

void task2(){
    std::cout << std::endl << "Task 2" << std::endl;
    double a = 1.5;
    inverse(a);
    std::cout << "Preference:" << a << std::endl;
    a = 1.5;
    inverse(&a);
    std::cout << "Pointers:" << a << std::endl;
}

void task3(){
    std::cout << std::endl << "Task 3" << std::endl;
    circle circle;
    circle.x = 0;
    circle.y = 0;
    circle.r = 5;
    double new_r = 2;
    //std::cin >> circle.x >> circle.y >> circle.r >> new_r;
    decrease(circle, new_r);
    std::cout << "Preference:" << circle.r << std::endl;
    circle.x = 0;
    circle.y = 0;
    circle.r = 5;
    new_r = 2;
    decrease(&circle, &new_r);
    std::cout << "Pointers:" << circle.r << std::endl;
}

void task4(){
    std::cout << std::endl << "Task 4" << std::endl;
    int temp [3][3] =  {{1,1,1}, {2,2,2}, {3,3,3}};
    int line1 = 1, line2 = 2;
    matrix matrix;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            matrix.elements[i][j] = temp[i][j];

    change_lines(matrix, line1, line2);
    std::cout << "Preference:" << std::endl;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++)
            std::cout << matrix.elements[i][j] << " ";
    std::cout << std::endl;
    }

    change_lines(&matrix, &line1, &line2);
    std::cout << "Pointers:" << std::endl;
    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++)
            std::cout << matrix.elements[i][j] << " ";
    std::cout << std::endl;
    }
}
int main(){
    task1();
    task2();
    task3();
    task4();
}
