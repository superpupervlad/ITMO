#include <iostream>
#include "GeomObjects.h"
#include <vector>
#include <algorithm>

int main() {
    std::vector<AllInOne*> Figures;
    system("clear");
    int command=0;
    int command2 = 0;
    while (command != 8){
        command = 0;
        command2 = 0;
        std::cout << "1. Add figure" << "\n";
        std::cout << "2. Show all figures" << "\n";
        std::cout << "3. Sum of all areas" << "\n";
        std::cout << "4. Sum of all perimeters" << "\n";
        std::cout << "5. Show center of the system" << "\n";
        std::cout << "6. Show total memory" << "\n";
        std::cout << "7. Sort figures" << "\n";
        std::cout << "8. Exit" << "\n";
        std::cin >> command;
        std::cout << "\n";
        switch (command){
            case 1:
                std::cout << "What figure do you want to add?\n";
                std::cout << "1. Circle\n";
                std::cout << "2. Rectangle\n";
                std::cin >> command2;
                if (command2 == 1){
                        Figures.push_back(new Circle());
                        break;
                }
                else if (command2 == 2){
                    Figures.push_back(new Rectangle());
                    break;
                }
                break;
            case 2:
                char t;
                system("clear");
                for (int i = 0; i < Figures.size(); i++){
                    std::cout << i + 1 << ".\n";
                    Figures[i]->draw();
                }
                std::cout << "Press any key to continue";
                std::cin >> t;
                break;
            case 3:{
                system("clear");
                double sum = 0;
                for (int i = 0; i < Figures.size(); i++)
                    sum += Figures[i]->square();
                std::cout << "Sum of all areas: " << sum << "\n";
                break;
            }
            case 4:{
                system("clear");
                double sum = 0;
                for (int i = 0; i < Figures.size(); i++)
                    sum += Figures[i]->perimeter();
                std::cout << "Sum of all perimeters: " << sum << "\n";
                break;
            }
            case 5:{
                system("clear");
                double total_mass = 0;
                CVector2D res;
                for (int i = 0; i < Figures.size(); i++){
                    res = res + Figures[i]->position()* Figures[i]->mass();
                    total_mass += Figures[i]->mass();
                }
                res = res / total_mass;
                std::cout << "Center of the system is ";
                res.PrintVector();
                break;
            }
            case 6:{
                system("clear");
                int sum = 0;
                for (int i = 0; i < Figures.size(); i++)
                    sum += Figures[i]->size();
                std::cout << "Total memory: " << sum << "\n";
                break;
            }
            case 7:{
                system("clear");
                sort(Figures.begin(), Figures.end(), [](AllInOne* x, AllInOne* y) {return *x < *y; });
                std::cout << "Figures sorted!\n";
                break;
            }
            case 8:
                return 0;
            default:
                system("clear");
                std::cout << "Bruh, you just posted cringe!\nTry again!\n";
                break;
        }
    }
}
