/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#pragma once
#include "Product.h"
#include "types/Ingredients.h"
#include <unordered_map>
#include <iostream>

class Burger final : public Product {
private:
    std::unordered_map<Ingredients, int> recipe_list;

public:
    Burger(const std::string &name_, const double quantity_, const std::unordered_map<Ingredients, int> &recipe_list)
        : Product(name_, quantity_),
          recipe_list(recipe_list) {
    }

    Burger() = default;

    double computeEnergy() override;

    ~Burger() override = default;
};
