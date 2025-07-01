#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

int main() {
  size_t len = 0;
  std::cin >> len;

  std::vector<std::string> arr(len);

  for (size_t i = 0; i < len; i++) {
    std::string current_string;
    std::cin >> current_string;

    if (current_string.length() % 2 != 0) {
      arr[i] = "NO";
    } else {
      arr[i] = "YES";
      for (size_t j = 0; j < current_string.length() / 2; j++) {
        if (current_string[j] != current_string[(current_string.length() / 2) + j]) {
          arr[i] = "NO";
        }
      }
    }
  }

  for (size_t i = 0; i < len; i++) {
    std::cout << arr[i] << '\n';
  }
}