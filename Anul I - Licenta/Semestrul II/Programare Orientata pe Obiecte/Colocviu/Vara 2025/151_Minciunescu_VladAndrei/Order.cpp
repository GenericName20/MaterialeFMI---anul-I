/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */


#include "Order.h"

[[nodiscard]] int Order::getId() const {
	return id;
}

double Order::computeTotalEnergy() const {
	double total_energy(0);
	for (const auto& product : this->product_list){
 		total_energy += product->computeEnergy();
	}

    return total_energy;
};

int Order::getProductCount() const {
	return product_list.size();
}
