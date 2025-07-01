#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
  std::string str;
  const int alphabed = 26;

  std::vector<int> weights(alphabed);
  std::vector<int> freq(alphabed, 0);
  std::vector<int> counted(alphabed, 0);

  std::cin >> str;

  for (int& weight : weights) {
    std::cin >> weight;
  }

  std::sort(str.begin(), str.end(), [&weights](char left, char right) {
    return weights[left - 'a'] > weights[right - 'a'];
  });

  std::string no_weight;
  std::string left;
  std::string right;

  for (const char current : str) {
    freq[current - 'a'] += 1;
  }

  for (const char current : str) {
    const int ind = current - 'a';
    counted[ind] += 1;

    if (freq[ind] - counted[ind] == 1 && freq[ind] >= 2) {
      left.push_back(current);
      continue;
    }

    if (freq[ind] - counted[ind] == 0 && freq[ind] >= 2) {
      right.push_back(current);
      continue;
    }

    if (freq[ind] == 1 || (freq[ind]) >= 2) {
      no_weight.push_back(current);
    }
  }

  std::reverse(right.begin(), right.end());
  std::cout << left + no_weight + right;
}