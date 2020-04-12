#pragma once
#include <iostream>

class Complex{
private:
    double re_;
    double im_;
public:
    Complex(); //По умолчанию
    Complex(double re, double im); //Вещественное/Комплексное
    Complex(const Complex& c); //Копирование
    ~Complex(); // Деструктор

    double len();
    
    double re();
    double im();
};

Complex operator* (Complex&, double);
Complex operator+ (Complex&, Complex&);
Complex operator* (Complex&, Complex&);
void print(Complex);
