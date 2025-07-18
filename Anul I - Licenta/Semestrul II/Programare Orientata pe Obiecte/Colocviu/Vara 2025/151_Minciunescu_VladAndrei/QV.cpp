/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#include "QV.h"

#include <Exceptions.h>
#include <iostream>
#include <format>
#include <unordered_map>


void QV::showEmployeeCount(const EmployeeType &tip_angajat) {
    std::unordered_map<EmployeeType, std::string> tipuri = {
        { EmployeeType::ChefWorker, "Bucatar" },
        { EmployeeType::CashierWorker, "Casier"},
        { EmployeeType::DeliveryWorker, "Livrator"}
    };

    int count(0);

    for (const auto& [id, employee] : employees) {
        if (const auto lvr = std::dynamic_pointer_cast<Delivery>(employee)
            && tip_angajat==EmployeeType::DeliveryWorker) {
            count++;
        } else if (const auto buc = std::dynamic_pointer_cast<Chef>(employee)
            && tip_angajat==EmployeeType::ChefWorker) {
            count++;
        } else if (const auto cas = std::dynamic_pointer_cast<Cashier>(employee)
            && tip_angajat==EmployeeType::CashierWorker) {
            count++;
        }
    }

    std::cout << std::format("> Angajati cu meseria de {}: {}\n", tipuri[tip_angajat], count);
}

void QV::simultateCycle(bool optimized) {
    std::shared_ptr<QVStrategy> strategy;
    int strategy_id, answer, prior_id;

    std::cout << "== START ==" << std::endl;

    // 3. Between cycles, choose prior orders
    // 0.5 for half-implementation
    std::cout << "== Alege comanda prioritara ==" << std::endl;
    std::cin >> prior_id;

    // 5. Order-choosing strategy
    std::cout << "== Alege strategia ==" << std::endl;
    std::cin >> strategy_id;
    switch (strategy_id) {
        case 0:  strategy = std::make_shared<MinEnergy>(); break;
        case 1: strategy = std::make_shared<MaxEnergy>(); break;
        case 2: strategy = std::make_shared<ProductCount>(); break;
        default: strategy = nullptr;
    }

    std::cout << "Adaugare comanda? (1/0)";
    std::cin >> answer;
     while (answer == 1) {
         std::vector<int> preferences = {0, 2, 3};
         std::set<std::shared_ptr<Product>> temp_prod_list;
         for (auto id : preferences) {
             if (menu.contains(id)) {
                 temp_prod_list.emplace(menu[id]);
             } else {
                 throw InvalidId(id);
             }
         }
         Order temp(temp_prod_list);
         orders[temp.getId()] = std::make_shared<Order>(temp);

         std::cout << "== Comenzi actuale ==" << std::endl;
         for (auto [id, order] : orders) {
             std::cout << std::format("Comanda #{} - Energie {}", id, order->computeTotalEnergy()) << std::endl;
         }

         std::cout << "Adaugare comanda? (1/0)";
         std::cin >> answer;
     }

    if (prior_id < 0) {
        std::vector<std::shared_ptr<Order>> smartOrders;
        if (strategy) {
            smartOrders = strategy->applyStrategy(orders);
        } else {
            for (auto [id, order] : orders) {
                smartOrders.push_back(order);
            }
        }

        std::cout << "== Comenzi strategice ==" << std::endl;
        for (const auto order : smartOrders) {
            std::cout << std::format("Comanda cu energia {}", order->computeTotalEnergy()) << std::endl;
        }
    } else {
        if (orders.contains(prior_id)) {
            std::shared_ptr<Order> prior_order = orders[prior_id];
        } else {
            prior_id = -1;
        }
    }

    std::cout << "== END ==" << std::endl;
}

void QV::setEmployees(const std::set<std::shared_ptr<Employee>>& temp) {
    try {
        employees.clear();

        for (const auto& employee : temp) {
            this->employees[employee->getId()] = employee;
        }
    } catch (EmployeesDefinition& e) {
        throw e;
    }

    if (employees.empty()) {
        throw EmployeesEmpty();
    }
}

void QV::setMenu(const std::set<std::shared_ptr<Product>>& temp) {
    try {
        menu.clear();
        for (const auto& product : temp) {
            this->menu[product->getId()] = product;
        }
    } catch (MenuDefinition& e) {
        throw e;
    }

    if (menu.empty()) {
        throw MenuEmpty();
    }
}