#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int a = 0;

  std::vector<int> val(4, 0);

  int now = 1;
  int result = 0;

  std::cin >> a;
  for (int i = 0; i < 4; i++) {
    std::cin >> val[i];
  }

  while (now <= val[3]) {
    const int a_start = a;

    a = a * val[0];

    a = (a >= val[1]) ? a - val[1] : 0;

    a = std::min(a, val[2]);

    if (now == val[3] and a != 0) {
      result = a;
      break;
    }

    if (a == 0) {
      result = 0;
      break;
    }

    if (a == a_start) {
      result = a;
      break;
    }

    now += 1;
  }

  std::cout << result;
}