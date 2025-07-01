#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

bool static CmpStrings(std::string const& left, std::string const& right) {
  return left + right > right + left;
}

int main() {
  std::vector<std::string> numbs;
  std::string current_srt;

  while (std::cin >> current_srt) {
    numbs.push_back(current_srt);
  }

  std::sort(numbs.begin(), numbs.end(), CmpStrings);

  for (const auto& numb : numbs) {
    std::cout << numb << "";
  }
}