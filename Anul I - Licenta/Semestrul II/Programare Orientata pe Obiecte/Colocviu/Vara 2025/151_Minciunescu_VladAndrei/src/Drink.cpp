/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#include "Drink.h"

double Drink::computeEnergy() {
    return this->bottle ? 25 : 0.25 * this->quantity;
}