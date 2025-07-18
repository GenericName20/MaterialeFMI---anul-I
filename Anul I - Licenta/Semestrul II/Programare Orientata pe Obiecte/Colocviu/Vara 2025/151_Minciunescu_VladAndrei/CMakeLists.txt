cmake_minimum_required(VERSION 3.30)
project(151_Minciunescu_VladAndrei)

set(CMAKE_CXX_STANDARD 20)

file(GLOB_RECURSE TEST_SRC
        src/*.cpp
)

add_executable(151_Minciunescu_VladAndrei
        main.cpp
        ${TEST_SRC}
        include/Product.h
        include/Drink.h
        include/Desert.h
        include/Burger.h
        src/Desert.cpp
        src/Burger.cpp
        src/Drink.cpp
        include/Employee.h
        include/Cashier.h
        src/Cashier.cpp
        include/Delivery.h
        src/Delivery.cpp
        include/Chef.h
        src/Chef.cpp
        QV.h
        Order.h
        QV.cpp
        Order.cpp
)

target_include_directories(151_Minciunescu_VladAndrei PUBLIC include)
