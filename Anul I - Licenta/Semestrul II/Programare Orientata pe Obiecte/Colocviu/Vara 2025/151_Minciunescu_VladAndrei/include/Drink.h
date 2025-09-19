/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#pragma once
#include "Product.h"
#include <iostream>

class Drink final : public Product{
private:
  bool bottle{};

public:
  Drink(const std::string &name_, const double quantity_, const bool bottle = false)
    : Product(name_, quantity_),
      bottle(bottle) {
  }
  // 0.25p - Inheritance (Usage of Product() in Drink())

  Drink() = default;

  double computeEnergy() override;

  // 0.25p - Virtual Destructor (it should be placed everywhere it is needed)
  ~Drink() override = default;
};
