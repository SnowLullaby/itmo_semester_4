#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int n = 0;
  int k = 0;
  std::cin >> n >> k;

  std::vector<int> prises(n);
  for (int& prise : prises) {
    std::cin >> prise;
  }

  std::sort(prises.begin(), prises.end());

  int sum = 0;
  int counter = 0;

  for (int i = n - 1; i >= 0; i--) {
    counter += 1;
    if (counter % k != 0) {
      sum += prises[i];
    } else {
      counter = 0;
    }
  }

  std::cout << sum;
}