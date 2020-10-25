#include <iostream>
#include <vector>
#include "iterators.h"
//#include <algorithm>

struct Animal{
    const char* name;
    const char* personal_name;
    unsigned weight;
    unsigned age;
    bool operator> (int a) {return (weight > a);}
    Animal(const char* name_, const char* pn, unsigned w, unsigned a) : name(name_), personal_name(pn), weight(w), age(a) {};
    ~Animal() = default;
};

template <class T>
bool is_positive(T& x){
    return (x > 0) ? true : false;
}

template <class T>
bool is_big(const T& x){
    return (x > 500) ? true : false;
}

int main() {
    std::vector<int> a{1, 2, -3, 2, 1};
    
    if (all_of(a.begin(), a.end(), is_positive<int&>))
        std::cout << "Predicate return true for all elements\n";
    else
        std::cout << "Predicate did not return true for all elements\n";

    if (is_partitioned(a.begin(), a.end(), is_positive<int&>))
        std::cout << "Partitioned\n";
    else
        std::cout << "Not partitioned\n";

    if (is_palindrome(a.begin(), a.end(), is_positive<int&>))
        std::cout << "Palindrome\n";
    else
        std::cout << "Not palindrome\n";
/*------------------------------------------------------------*/
    std::vector<Animal> zoo;
    zoo.push_back({"Lion", "Leon", 190, 5});
    zoo.push_back({"Monkey", "Miguel", 20, 25});
    zoo.push_back({"Crocodile", "Charlie", 800, 50});
    zoo.push_back({"Hippo", "Henry", 1500, 20});
    zoo.push_back({"Elephant", "Eric", 4000, 60});
    zoo.push_back({"Whale", "William", 50000, 40});
    
    if (all_of(zoo.begin(), zoo.end(), is_big<Animal&>))
        std::cout << "[Z] Predicate return true for all elements\n";
    else
        std::cout << "[Z] Predicate did not return true for all elements\n";

    if (is_partitioned(zoo.begin(), zoo.end(), is_big<Animal&>))
        std::cout << "[Z] Partitioned\n";
    else
        std::cout << "[Z] Not partitioned\n";

    if (is_palindrome(zoo.begin(), zoo.end(), is_big<Animal&>))
        std::cout << "[Z] Palindrome\n";
    else
        std::cout << "[Z] Not palindrome\n";
//     if (std::any_of(zoo.begin(), zoo.end(), is_big<Animal&>))
//         std::cout << "YYY";
    
    return 0;
}
