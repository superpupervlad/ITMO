#include <iostream>
#include <algorithm>
#include "circular_buffer.h"
#include "circular_buffer.cpp"

bool x(int z){
    return (z < 0);
}

int main() {
    CB<int> a(10);
    a.pushright(1);
    a.pushright(-5);
    a.pushright(3);
    a.pushright(9);
    a.pushright(4);
    a.print();
    std::cout << "Сортировка\n";
    
    std::sort(a.begin(), a.end());
    a.print();
    if (std::any_of(a.begin(), a.end(), x))
        std::cout << "Есть отрицательное число\n";

    std::cout << "Пример переполнения\n";
    for(int i = 0; i < 10; i++){
        a.pushright(i);
        a.print();
    }
    std::cout << "Вывод последнего введенного элемента\n";
    std::cout << a.peekright() << '\n';
    std::cout << "Вывод всех элементов с конца\n";
    while(!a.empty())
    {
        std::cout << a.popright() << " ";
    }
    std::cout << '\n';
    std::cout << "Пример изменения размера\n";
    a.change_size(7);
    a.print();
    for(int i = 0; i < 10; i++){
        a.pushright(i);
        a.print();
    }
    std::cout << "Пример добавления элемента слева\n";
    a.pushleft(99);
    a.print();
    return 0;
}

