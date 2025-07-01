#include <cctype>
#include <cstddef>
#include <iostream>
#include <stack>
#include <string>
#include <vector>

int main() {
  std::string str;
  std::cin >> str;

  int numb_trp = 0;
  int numb_ani = 0;

  std::vector<int> path(str.length() / 2);

  std::stack<char> stk_animals;
  std::stack<int> stk_numbers;

  for (size_t i = 0; i < str.length(); i++) {
    const char curr_letter = str[i];

    if (std::isupper(curr_letter) != 0) {
      numb_trp += 1;
    } else {
      numb_ani += 1;
    }

    if (!stk_animals.empty() && (std::tolower(stk_animals.top()) == std::tolower(curr_letter)) &&
        (stk_animals.top() != curr_letter)) {
      if (std::isupper(stk_animals.top()) != 0) {
        path[stk_numbers.top() - 1] = numb_ani;
      } else {
        path[numb_trp - 1] = stk_numbers.top();
      }

      stk_animals.pop();
      stk_numbers.pop();
      continue;
    }

    stk_animals.push(curr_letter);

    if (std::isupper(curr_letter) != 0) {
      stk_numbers.push(numb_trp);
    } else {
      stk_numbers.push(numb_ani);
    }
  }

  if (stk_animals.empty()) {
    std::cout << "Possible" << '\n';
    for (const int num : path) {
      std::cout << num << " ";
    }
  } else {
    std::cout << "Impossible" << '\n';
  }
}