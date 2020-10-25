#pragma once
#include <memory> // Для умных указателей
#include <string.h> // memcpy
#include <cstdlib> // rand
#include <fstream> // files
#include <vector> // for operations

void cpy_left_turn();

class Kubik;
class Side;
class A;
class B;

class Side{
public:
    Side(char c);
    ~Side() = default;

    char main_color;
    char data[3][3];
    bool check();
    void p(); // print
    void file_print(FILE *f);
};

class Kubik{
public:
    Kubik();
    ~Kubik() = default;
    //Front        - Black Purple
    Side F = Side{'B'}; 
    //Up            - Purple
    Side U = Side{'P'};
    //Back   - Orange
    Side B = Side{'O'};
    //Down        - Cyan
    Side D = Side{'C'};
    //Right         - Green
    Side R = Side{'G'};
    //Left          - Yellow
    Side L = Side{'Y'};
    Side* sides[6] = {&F, &U, &B, &D, &R, &L};
    bool correct;
    std::vector<char> operations; // f = clockwise F = counter-clockwise
    void print(); // print
    void frotate(bool clockwise = 1, bool check = 1);
    void lrotate(bool clockwise = 1, bool check = 1);
    void rrotate(bool clockwise = 1, bool check = 1);
    void urotate(bool clockwise = 1, bool check = 1);
    void drotate(bool clockwise = 1, bool check = 1);
    void brotate(bool clockwise = 1, bool check = 1);
    void randomize(int number_of_turns = 10);
    bool check();
    void file_print(FILE *f);
    void save();
    void load();
    void solve();
};




