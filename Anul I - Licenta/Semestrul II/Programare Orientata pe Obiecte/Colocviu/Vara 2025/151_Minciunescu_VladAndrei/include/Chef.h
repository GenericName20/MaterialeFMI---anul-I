/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#pragma once
#include "Employee.h"

class Chef final : public Employee{
public:
    explicit Chef(const std::optional<float> &energy_points_)
        : Employee(energy_points_) {
    }

    void useEnergy() override;

    ~Chef() override = default;
};
