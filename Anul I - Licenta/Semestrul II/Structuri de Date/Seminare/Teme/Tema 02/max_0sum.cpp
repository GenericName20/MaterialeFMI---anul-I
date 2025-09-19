#include <iostream>
#include <vector>
#include <random>
#include <unordered_map>

int random_value() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> range(0, 1);
    return range(gen);
}
int main() {
    int n;
    std::cin >> n;
    std::vector<int> A(n);
    std::unordered_map<int, int> sum;

    for (int i = 0; i < n; ++i) {
        A[i] = random_value();
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    int prefix_sum = 0, length = 0;

    for (int i = 0; i < n; i++) {
        prefix_sum += A[i] == 0 ? -1 : 1;

        if (prefix_sum == 0) {
            length = i + 1;
        }
      
        if (sum.find(prefix_sum) != sum.end()) {
            length = std::max(length, i - sum[prefix_sum]);
        }
        else {
            sum[prefix_sum] = i;
        }
    }
    
    std::cout << length;
    return 0;
}