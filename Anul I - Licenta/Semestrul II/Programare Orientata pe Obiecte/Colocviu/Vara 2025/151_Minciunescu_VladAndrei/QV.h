/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

#pragma once

#include "Burger.h"
#include "Desert.h"
#include "Drink.h"
#include "Delivery.h"
#include "Chef.h"
#include "Cashier.h"

#include "Employee.h"

#include "Order.h"
#include "types/EmployeeType.h"

#include <unordered_map>
#include <memory>
#include <queue>
#include <algorithm>

// 1p - Strategy Pattern
// 0.25p - STL Utility (std::sort)
class QVStrategy {
public:
    virtual std::vector<std::shared_ptr<Order>> applyStrategy(std::unordered_map<int, std::shared_ptr<Order>> orders) const = 0;
    virtual ~QVStrategy() = default;
};

class MinEnergy final : public QVStrategy {
public:
    std::vector<std::shared_ptr<Order>> applyStrategy(std::unordered_map<int, std::shared_ptr<Order>> orders) const override {
        std::vector<std::pair<int, std::shared_ptr<Order>>> temp;

        for (auto& [id, order] : orders) {
            int energy = order->computeTotalEnergy();
            temp.emplace_back(energy, order);
        }

        std::ranges::sort(temp, [](auto& a, auto& b) {
            return a.first < b.first;
        });

        std::vector<std::shared_ptr<Order>> result;
        for (auto& [energy, order] : temp) {
            result.push_back(order);
        }

        return result;
    }
};

class MaxEnergy final : public QVStrategy {
public:
    std::vector<std::shared_ptr<Order>> applyStrategy(std::unordered_map<int, std::shared_ptr<Order>> orders) const override {
        std::vector<std::pair<int, std::shared_ptr<Order>>> temp;

        for (auto& [id, order] : orders) {
            int energy = order->computeTotalEnergy();
            temp.emplace_back(energy, order);
        }

        std::ranges::sort(temp, [](auto& a, auto& b) {
            return a.first > b.first;
        });

        std::vector<std::shared_ptr<Order>> result;
        for (auto& [energy, order] : temp) {
            result.push_back(order);
        }

        return result;
    }
};

class ProductCount final : public QVStrategy {
public:
    std::vector<std::shared_ptr<Order>> applyStrategy(std::unordered_map<int, std::shared_ptr<Order>> orders) const override {
        std::vector<std::pair<int, std::shared_ptr<Order>>> temp;

        for (auto& [id, order] : orders) {
            int count = order->getProductCount();
            temp.emplace_back(count, order);
        }

        std::ranges::sort(temp, [](auto& a, auto& b) {
            return a.first > b.first;
        });

        std::vector<std::shared_ptr<Order>> result;
        for (auto& [count, order] : temp) {
            result.push_back(order);
        }

        return result;
    }
};

// 0.25p - STL Containers (unordered_map, set, vector)
// 0.25p - Static
// 0.25p - Singleton
class QV {
private:
    std::unordered_map<int, std::shared_ptr<Employee>> employees;
    std::unordered_map<int, std::shared_ptr<Product>> menu;

    std::unordered_map<int, std::shared_ptr<Order>> orders;

    // fara greater<> ca vrem heap de max
    // std::priority_queue<std::pair<float, std::shared_ptr<Order>>> comenzi_prioritare;

    QV() : employees({}), menu({}), orders({}) {}

public:
    static QV &getInstance() {
        static QV instance;
        return instance;
    }

    QV(const QV&) = delete;
    QV &operator=(const QV&) = delete;

    void addEmployee(const EmployeeType& employee_type, float energy_points_);

    void setEmployees(const std::set<std::shared_ptr<Employee>>& temp);

    void setMenu(const std::set<std::shared_ptr<Product>>& temp);

    void showEmployeeCount(const EmployeeType& employee_type);

    void simultateCycle(bool optimized = false);

    ~QV() = default;
};
