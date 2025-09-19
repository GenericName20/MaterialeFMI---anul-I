/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#include "Burger.h"

double Burger::computeEnergy() {
    return this->quantity * 0.25 * static_cast<double>(recipe_list.size());
}
