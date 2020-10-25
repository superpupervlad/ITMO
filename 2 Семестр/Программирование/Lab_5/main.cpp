#include "Functions_and_exceptions.h"
#include <iostream>
using namespace std;

int main (){
    int first = 1;
    int second = 2;
    cout << "first: " << first << " second: " << second << '\n';
    myswap(first, second);
    cout << "first: " << first << " second: " << second << '\n';
    cout << "-----------------\n";
    Array <10, int> a;
    try{
        cout << a[-1];
    } catch (Exception &error){
        cout << "Error: " << error.what();
    }
}
