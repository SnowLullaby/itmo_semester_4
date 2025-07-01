#include <array>
#include <cstddef>
#include <iostream>

int main() {
  size_t numb = 0;
  std::cin >> numb;

  size_t beg = 0;
  size_t end = 0;

  size_t max_beg = 0;
  size_t max_end = 0;

  std::array<int, 3> arr = {0, 0, 0};

  std::cin >> arr[0];

  if (numb >= 2) {
    std::cin >> arr[1];
    end = 1;
    max_end = 1;
  }

  for (size_t i = 2; i < numb; i++) {
    std::cin >> arr[2];
    if (arr[0] == arr[1] and arr[1] == arr[2]) {
      if (end - beg > max_end - max_beg) {
        max_end = end;
        max_beg = beg;
      }
      beg = end;
    }

    end += 1;
    arr[0] = arr[1];
    arr[1] = arr[2];
  }

  if (end - beg > max_end - max_beg) {
    max_end = end;
    max_beg = beg;
  }

  std::cout << max_beg + 1 << " " << max_end + 1 << '\n';
}