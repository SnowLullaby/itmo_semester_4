#include <cstddef>
#include <iostream>
#include <vector>

int main() {
  size_t n = 0;
  std::cin >> n;

  size_t cows = 0;
  std::cin >> cows;

  std::vector<int> stalls(n);
  for (size_t i = 0; i < n; i++) {
    std::cin >> stalls[i];
  }

  int start = -1;
  int end = stalls[n - 1] - stalls[0] + 1;

  while (end - 1 > start) {
    size_t prev_cow_place = 0;
    size_t left_to_place = cows - 1;
    const int delta = (end + start) / 2;

    for (size_t i = 0; i < n; i++) {
      if (stalls[i] - stalls[prev_cow_place] >= delta) {
        prev_cow_place = i;
        left_to_place -= 1;
      }

      if (left_to_place == 0) {
        break;
      }
    }

    if (left_to_place > 0) {
      end = delta;
    }

    if (left_to_place == 0) {
      start = delta;
    }
  }

  std::cout << start;
}