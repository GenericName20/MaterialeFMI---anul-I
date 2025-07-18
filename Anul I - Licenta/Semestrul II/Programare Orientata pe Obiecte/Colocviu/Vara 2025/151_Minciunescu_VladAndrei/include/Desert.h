/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#pragma once

#include "Product.h"
#include "types/ServiceType.h"

#include <iostream>

class Desert final : public Product {
private:
  ServiceType tip;

public:
  Desert(const std::string &name_, const double quantity_, const ServiceType& tip = ServiceType::Unknown)
    : Product(name_, quantity_),
      tip(tip) {}
  // 0.25p - Validarea tipului de desert cu enum

  Desert() = default;

  double computeEnergy() override;

  ~Desert() override = default;
};
