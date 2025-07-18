#include "vector.h"
#include "tests.cpp"

int main() {
    test::default_allocator();
    test::sized_allocator();
    test::random_access();
    test::sized_value_allocator();
    test::front_back();
    test::front_back_const();
    test::print_vector();
    test::begin_end();
    test::push_back();
    test::pop_back();
    test::clear();
    test::resize();
    test::reserve();
    test::shrink_to_fit();

    return 0;
}
