#include <iostream>
#include <sstream>
#include <unordered_map>
#include <string>

class Solution {
public:
    std::vector<int> findSubstring(std::string s, std::vector<std::string>& words) {
        int word_length(words[0].size());
        if (word_length > s.size()) {
            return std::vector<int>();
        }

        // Set every word's frequency in given list
        std::unordered_map<std::string, int> words_map;

        /*
            if (words_map.find(word) == words_map.end()) {
                words_map[word] = 0;
            }
        */
        words_map.clear();

        for (std::string word : words) {
            ++words_map[word];
        }

        // Find words_map from given list, in the first string
        std::vector<std::string> start(s.size(), "");
        for (int i = 0; i <= s.length() - word_length; ++i) {
            std::string current_word;
            current_word = s.substr(i, word_length);
            if (words_map.find(current_word) != words_map.end()) {
                // Set every word to the position it belongs to, in the first string
                start[i] = current_word;
            }
        }

        // Find subarrays of concatenated words_map from the given list
        std::vector<int> result;
        for (int i = 0; i < s.size(); ++i) {
            if (start[i] != "") {
                std::unordered_map<std::string, int> subarray;
                subarray[start[i]] = 1;
                for (int j = i + word_length;
                    j < s.size()
                    && start[j] != ""
                    && words_map.find(start[j]) != words_map.end();
                    j += word_length) {
                    if (subarray.find(start[j]) == subarray.end()) {
                        subarray[start[j]] = 1;
                    }
                    else if (subarray[start[j]] < words_map[start[j]]) {
                        ++subarray[start[j]];
                    }
                    else {
                        break;
                    }
                }

                if (subarray.size() == words_map.size()) {
                    bool concat(true);
                    for (auto& pair : subarray) {
                        if (subarray[pair.first] != words_map[pair.first]) {
                            concat = false;
                            break;
                        }
                    }

                    if (concat) {
                        result.push_back(i);
                    }
                }
            }
        }

        return result;
    };
};

int main() {
    std::string s;
    std::getline(std::cin, s);

    std::string all_words;
    std::getline(std::cin, all_words);

    std::stringstream ss(all_words);
    std::string word;
    std::vector<std::string> words;
    while (ss >> word) {
        words.push_back(word);
    }

    Solution sol;
    for (auto it : sol.findSubstring(s, words)) {
        std::cout << it << " ";
    }
    return 0;
}