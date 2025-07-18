/* Minciunescu Vlad - 151
CLion MinGW | See CMakeLists.txt
Livia Magureanu */

// This colloquium would have scored somewhere between 11 ~ 12 points.

#include <iostream>
#include "QV.h"
#include "Exceptions.h"

int main() {
    QV& app = QV::getInstance();

    // 0. Employee setup (With energy points presumtion)
    // For more 0.25p create a factory class
    try {
        app.setEmployees({
            std::make_shared<Delivery>(100),
            std::make_shared<Chef>(125), std::make_shared<Chef>(100),
            std::make_shared<Cashier>(100), std::make_shared<Cashier>(200)
        });
    } catch (EmployeesDefinition& e) {
        std::cerr << e.what() << std::endl;
    } catch (EmployeesEmpty& e){
        std::cerr << e.what() << std::endl;
    } catch (std::exception& e){
        std::cerr << e.what() << std::endl;
    }

    // 0.5p - Menu setup
    try {
        app.setMenu({
            std::make_shared<Burger>("D-asta n-ai mai mancat", 450,
                std::unordered_map<Ingredients, int>{
                    {Ingredients::Beef, 3},
                    {Ingredients::Onion, 2},
                    {Ingredients::Tomato, 3}
            }),
            std::make_shared<Desert>("Inghetata degete lingi", 125, ServiceType::Cup),
            std::make_shared<Desert>("Clatite utza-utza", 200, ServiceType::Portion),
            std::make_shared<Drink>("Blugi cu banane", 500, true)
        });
    } catch (MenuDefinition& e) {
        std::cerr << e.what() << std::endl;
    } catch (MenuEmpty& e) {
        std::cerr << e.what() << std::endl;
    } catch (std::exception& e){
        std::cerr << e.what() << std::endl;
    }

    // 0.5p - Employee count using RTTI (dynamic_pointer_cast in this case)
    std::cout << "Subtask I" << std::endl;
    app.showEmployeeCount(EmployeeType::ChefWorker);
    app.showEmployeeCount(EmployeeType::CashierWorker);
    app.showEmployeeCount(EmployeeType::DeliveryWorker);

    // 2. Cycle simulation
    try {
        app.simultateCycle(false);
    } catch (InvalidId& e) {
        std::cerr << e.what() << std::endl;
    }

    // 3. Between cycles, choose prior orders
    // Half-implemented in cycle

    // 4. Optimized cycle, each employee will do his tasks

    // 5. Order-choosing strategy
    // Implemented in cycle

    return 0;
}