/// \copyright This code under WTFPL licence

#include <iostream>
#include "calc.cpp"

using namespace std;
/// \brief Show user friendly menu
void menu() {
    cout << "Enter operation sign or number\n";
    cout << "1. Addition +\n";
    cout << "2. Subtraction -\n";
    cout << "3. Multiplication *\n";
    cout << "4. Division /\n";
    char choice;
    cin >> choice;
    cout << "Now enter 2 numbers\n";
    float n1, n2;
    cin >> n1 >> n2;
    cout << processing_result(choice, n1, n2);
}

int main() {
    menu();
}