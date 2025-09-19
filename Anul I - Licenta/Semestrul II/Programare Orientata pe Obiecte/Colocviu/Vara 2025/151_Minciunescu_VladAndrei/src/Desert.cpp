/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#include "Desert.h"

double Desert::computeEnergy() {
    if (this->tip == ServiceType::Slice) {
        return 25;
    }
    if (this->tip == ServiceType::Portion) {
        return 0.5 * this->quantity;
    }
    if (this->tip == ServiceType::Cup) {
        return 2 * this->quantity;
    }
    return 0;
}