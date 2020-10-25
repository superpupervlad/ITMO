#include <iostream>
#include "Kubik.h"

using std::cout;

int main(int argc, char **argv) {
    cout << "Hello, world!" << std::endl;
    Kubik k;
    k.print();
    cout << "---------------------\n";
    k.randomize(7);
    k.save();
    k.print();
    cout << "---------------------\n";
    k.solve();
    k.print();
    return 0;
}
