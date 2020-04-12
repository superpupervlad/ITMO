#include "Array.h"

Array::Array(){
    this->size_ = 0;
}

Array::Array(int size){
    if (size > 100){
        std::cout << "ERROR!\nValue for this array too big!\n";
        return;
    }
    this->size_ = size;
    std::cout << "Write " << size << " numbers.\n";
    for (int i = 0; i < size; i++) 
        std::cin >> array_ [i];
}

Array::~Array() = default;

void Array::add(int n){
    if (this->size_ == 100){
        std::cout << "ERROR!\nValue for this array too big!\n";
        return;
    }
    this->array_ [size_ + 1] = n;
}

void Array::change_el(int cell, int value){
    if (cell > 100){
        std::cout << "ERROR!\nValue for this array too big!\n";
        return;
    }
    this->array_ [cell] = value;
}
void Array::change_size(int n){
    this->size_ = n;
}

int Array::get_size(){
    return this->size_;
}

int Array::get_el(int a){
    return this->array_[a];
}

Array operator+(Array& a1, Array& a2){
    Array arr;
    if (a1.get_size() + a2.get_size() > 100){
        for (int i = 0; i < a1.get_size(); i++)
            arr.add(a1.get_el(i));
        for (int i = 0; arr.get_size() < 100; i++)
            arr.add(a1.get_el(i));
        return arr;
    }
    for (int i = 0; i < a1.get_size(); i++)
        arr.change_el(i, a1.get_el(i));
    for (int i = 0; i < a2.get_size(); i++)
        arr.change_el(a1.get_size() + i, a2.get_el(i));
    arr.change_size(a1.get_size() + a2.get_size());
    return arr;
}

bool operator== (Array& a1, Array& a2){
    return a1.get_size() == a2.get_size();
}

bool operator> (Array& a1, Array& a2){
    return a1.get_size() > a2.get_size();
}

bool operator< (Array& a1, Array& a2){
    return a1.get_size() < a2.get_size();
}

bool operator!= (Array& a1, Array& a2){
    return a1.get_size() != a2.get_size();
}

void print(Array a){
    std::cout << "COUNT\t|\tVALUE\n";
    for (int i = 0; i < a.get_size(); i++)
        std::cout  << i << "\t|\t" << a.get_el(i) << "\n";
}
