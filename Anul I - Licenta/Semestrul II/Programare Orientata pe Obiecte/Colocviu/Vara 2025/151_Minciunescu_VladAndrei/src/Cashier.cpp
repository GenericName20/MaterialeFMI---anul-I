/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#include "Cashier.h"

#include <iostream>

void Cashier::useEnergy() {
    if (this->energy_points - 25 >= 0) {
        this->energy_points -= 25;
    } else {
        std::cout << "Failed to take the task";
    }
}