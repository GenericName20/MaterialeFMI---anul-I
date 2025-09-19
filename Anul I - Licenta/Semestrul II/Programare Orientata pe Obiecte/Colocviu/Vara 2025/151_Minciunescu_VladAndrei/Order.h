/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#pragma once
#include "Product.h"

#include <set>
#include <memory>

class Order {
private:
  static int inline id_counter = 0;
  int id;
  std::set<std::shared_ptr<Product>> product_list;

public:
  explicit Order(const std::set<std::shared_ptr<Product>> &product_list_)
    : id(id_counter++),     // 0.25p - Id Counter incremented in constructor
      product_list(product_list_) {
  }

  [[nodiscard]] int getId() const;

  [[nodiscard]] int getProductCount() const;

  // 0.25p - Compute order's energy
  [[nodiscard]] double computeTotalEnergy() const;

  ~Order() = default;
};
