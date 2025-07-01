#include <iostream>
#include <map>
#include <vector>

int main() {
  std::map<int, int> window;

  int n = 0;
  int k = 0;
  std::cin >> n >> k;

  std::vector<int> result;
  std::vector<int> data;

  for (int i = 0; i < n; i++) {
    int cur_numb = 0;
    std::cin >> cur_numb;
    data.push_back(cur_numb);
  }

  for (int i = 0; i < n; i++) {
    if (i >= k) {
      result.push_back(window.cbegin()->first);

      if (window[data[i - k]] == 1) {
        window.erase(data[i - k]);
      } else {
        window[data[i - k]] -= 1;
      }
    }

    if (window.find(data[i]) == window.end()) {
      window[data[i]] = 1;
    } else {
      window[data[i]] += 1;
    }
  }

  result.push_back(window.cbegin()->first);

  for (const int res : result) {
    std::cout << res << ' ';
  }
}