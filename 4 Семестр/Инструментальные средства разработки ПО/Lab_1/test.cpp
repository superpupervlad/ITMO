#include <iostream>
#include "calc.cpp"

using namespace std;

void test(char op, float n1, float n2, float answer) {
    if (processing_result(op, n1, n2) == answer)
        cout << n1 << " " << op << " " << n2 << " TEST PASSED\n";
    else
        cout << n1 << " " << op << " " << n2 << " TEST FAILED\n";
}

int main() {
    test('+', 1, 2, 3);
    test('-', 0, 123, -123);
    test('*', 3, 4, 12);
    test('/', 10, 5, 2);
}