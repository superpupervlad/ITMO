#pragma once
#include <iostream>

class Array{
private:
    int array_ [100];
    int size_;
public:
    Array();
    Array(int size);
    ~Array();

    void add(int);
    void change_el(int, int);
    void change_size(int);
    int get_size();
    int get_el(int);
};

Array operator+ (Array&, Array&);
bool operator== (Array&, Array&);
bool operator> (Array&, Array&);
bool operator< (Array&, Array&);
bool operator!= (Array&, Array&);
void print(Array);
