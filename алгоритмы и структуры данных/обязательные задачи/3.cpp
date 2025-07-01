#include <cstddef>
#include <iostream>
#include <set>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

namespace {
bool TryToConvert(const std::string& str) {
  try {
    std::stoi(str);
    return true;
  } catch (const std::invalid_argument& e) {
    return false;
  }
}

std::vector<int> Funk(
    std::vector<std::string>& arr, std::unordered_map<std::string, int>& dict, size_t& start
) {
  std::unordered_map<std::string, int> backup;
  std::vector<int> res;

  while (start < arr.size()) {
    if (arr[start] == "{") {
      start++;
      std::vector<int> res_inside = Funk(arr, dict, start);
      res.insert(res.end(), res_inside.begin(), res_inside.end());
      continue;
    }

    if (arr[start] == "}") {
      start++;
      break;
    }

    const size_t pos = arr[start].find('=');
    const std::string var = arr[start].substr(0, pos);
    const std::string value = arr[start].substr(pos + 1);

    if (backup.find(var) == backup.end()) {
      backup[var] = dict[var];
    }

    if (TryToConvert(value)) {
      dict[var] = std::stoi(value);
    } else {
      dict[var] = dict[value];
      res.push_back(dict[value]);
    }

    start++;
  }

  for (const auto& var : backup) {
    dict[var.first] = var.second;
  }
  return res;
}
}  // namespace

int main() {
  std::vector<std::string> arr;
  std::string current_srt;
  std::unordered_map<std::string, int> dict;
  size_t start = 0;

  while (std::cin >> current_srt) {
    arr.push_back(current_srt);
  }

  for (const int num : Funk(arr, dict, start)) {
    std::cout << num << '\n';
  }
}