#include <deque>
#include <iostream>
#include <string>
#include <vector>

int main() {
  int n = 0;
  std::cin >> n;

  std::deque<int> first_half;
  std::deque<int> second_half;

  std::vector<int> result;

  for (int i = 0; i < n; i++) {
    std::string curr_str;
    std::cin >> curr_str;
    int curr_numb = 0;

    if (curr_str[0] == '-') {
      result.push_back(first_half.front());
      first_half.pop_front();

      if (first_half.size() < second_half.size()) {
        first_half.push_back(second_half.front());
        second_half.pop_front();
      }
    }

    if (curr_str[0] == '*') {
      std::cin >> curr_numb;

      if (first_half.size() > second_half.size()) {
        second_half.push_front(curr_numb);
      } else {
        first_half.push_back(curr_numb);
      }
    }

    if (curr_str[0] == '+') {
      std::cin >> curr_numb;
      second_half.push_back(curr_numb);

      if (first_half.size() < second_half.size()) {
        first_half.push_back(second_half.front());
        second_half.pop_front();
      }
    }
  }

  for (const int res : result) {
    std::cout << res << '\n';
  }
}