/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#pragma once

#include <string>
#include <utility>

class Product {
protected:
    static int inline id_counter = 0;
    int id;
    std::string name;
    double quantity;

public:
    Product() : id(id_counter++), name("Secret product"), quantity(0) {
    };

    Product(std::string name_, const double quantity_)
        : id(id_counter++), name(std::move(name_)), quantity(quantity_) {

    }

    [[nodiscard]] int getId() const;

    // 0.25p - Compute product's energy
    // 0.25p - Abstract (better defined at QVStrategy)
    virtual double computeEnergy() = 0;

    virtual ~Product() = default;
};
