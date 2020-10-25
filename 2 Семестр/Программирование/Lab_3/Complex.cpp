#include "Complex.h"
#include <math.h>

Complex::Complex():
    re_(0),
    im_(0)
{}

Complex::Complex(double re, double im = 0): 
    re_(re),
    im_(im)
{}

Complex::Complex(const Complex& c){
    this->re_ = c.re_;
    this->im_ = c.re_;
}

Complex::~Complex() = default; // Возможно не нужен

Complex::operator double(){
    return sqrt(pow(this->re(), 2) + pow(this->im(), 2));
}

double Complex::re(){
    return this->re_;
}

double Complex::im(){
    return this->im_;
}

Complex operator* (Complex& c, double r){
    return Complex(c.re() * r, c.im() * r);
}

Complex operator+ (Complex& c1, Complex& c2){
    return Complex(c1.re() + c2.re(), c1.im() + c2.im());
}

Complex operator* (Complex& c1, Complex& c2){
    return Complex(c1.re()*c2.re() - c1.im()*c2.im(),
                   c1.re()*c2.im() + c1.im()*c2.re());
}
void print(Complex c){
    std::cout << c.re() << " + " << c.im() << "i\n"; 
}
