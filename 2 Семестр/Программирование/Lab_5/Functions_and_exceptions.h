#pragma once
#include <string>
#include <iostream>
#include <exception>

class Exception : public std::exception{
public:
    Exception(const char* error_){
        error = error_;
    };

    const char* what() noexcept{
        return error;
    };

    const char* error;
};

template <typename T>
void myswap(T& a, T& b){
    T temp = a;
    a = b;
    b = temp;
}

template <int size_, typename T> 
class Array{
public:
    int size = size_;
    T* arr;
    Array();
    T& operator[](int a);
};

template <int size_, typename T>
Array<size_, T>::Array(){
    size = size_;
    arr = new T[size];
}

template <int size_, typename T>
T& Array<size_, T>::operator[](int a){
    if (a < 0 or a > size_)
        throw Exception("Index out of range!\n");
    else
        return arr[a];
}
