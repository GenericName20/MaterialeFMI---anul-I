#pragma once

#include <format>
#include <exception>
class EmployeesEmpty final : public std::exception {
public:
    const char* what() const noexcept override {
        return "Employee list is empty";
    }
};

class EmployeesDefinition final : public std::exception {
public:
    const char* what() const noexcept override {
        return "Employee list is not correctly defined";
    }
};

class MenuEmpty final : public std::exception {
public:
    const char* what() const noexcept override {
        return "Product list is empty";
    }
};

class MenuDefinition final : public std::exception {
public:
    const char* what() const noexcept override {
        return "Product list is not correctly defined";
    }
};

class InvalidId final : public std::exception {
    int id;
    std::string message;
public:
    explicit InvalidId(int id_) : id(id_) {
        message = std::format("The given ID ({}) is not an actual key", id);
    }

    const char* what() const noexcept override {
        return message.c_str();
    }
};