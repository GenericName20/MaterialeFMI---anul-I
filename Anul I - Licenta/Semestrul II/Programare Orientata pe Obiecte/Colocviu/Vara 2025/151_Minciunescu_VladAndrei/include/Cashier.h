/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#pragma once
#include "Employee.h"

class Cashier final : public Employee{
public:
    explicit Cashier(const std::optional<float> &energy_points_)
        : Employee(energy_points_) {
    }

    void useEnergy() override;

    ~Cashier() override = default;
};
