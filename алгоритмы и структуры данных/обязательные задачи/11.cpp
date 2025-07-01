#include <cstdlib>
#include <iostream>
#include <iterator>
#include <list>
#include <map>
#include <tuple>
#include <unordered_map>
#include <vector>

int main() {
  int n = 0;
  int m = 0;
  std::cin >> n >> m;
  std::cin.ignore();

  using Block = std::tuple<int, int, int>;

  std::list<Block> blocks;
  std::unordered_map<int, std::list<Block>::iterator> commands;
  std::multimap<int, std::list<Block>::iterator> free_blocks;
  std::vector<int> result;

  blocks.emplace_back(1, n, 0);
  free_blocks.emplace(n, prev(blocks.end()));

  for (int i = 1; i <= m; i++) {
    int value = 0;
    std::cin >> value;

    if (value < 0) {
      value = std::abs(value);

      if (commands[value] == blocks.end()) {
        continue;
      }

      auto block_it = commands[value];
      auto [start, size, status] = *block_it;

      auto next_it = std::next(block_it);

      if (block_it != blocks.begin()) {
        auto prev_it = std::prev(block_it);
        auto [prev_start, prev_size, prev_status] = *prev_it;
        if (prev_status == 0) {
          start = prev_start;
          size = prev_size + size;

          *block_it = {start, size, 0};

          auto same_size = free_blocks.equal_range(prev_size);
          for (auto it_map = same_size.first; it_map != same_size.second; it_map++) {
            if (it_map->second == prev_it) {
              free_blocks.erase(it_map);
              break;
            }
          }

          blocks.erase(prev_it);
        }
      }

      if (next_it != blocks.end()) {
        auto [next_start, next_size, next_status] = *next_it;
        if (next_status == 0) {
          size = next_size + size;

          *block_it = {start, size, 0};

          auto same_size = free_blocks.equal_range(next_size);
          for (auto it_map = same_size.first; it_map != same_size.second; it_map++) {
            if (it_map->second == next_it) {
              free_blocks.erase(it_map);
              break;
            }
          }

          blocks.erase(next_it);
        }
      }

      *block_it = {start, size, 0};
      free_blocks.emplace(size, block_it);

    } else {
      auto it = free_blocks.lower_bound(value);

      if (it == free_blocks.end()) {
        commands.emplace(i, blocks.end());
        result.push_back(-1);
        continue;
      }

      auto block_it = it->second;
      auto [start, size, status] = *block_it;
      free_blocks.erase(it);

      const int new_start = start + value;
      const int new_size = size - value;

      *block_it = {start, value, 1};
      commands.emplace(i, block_it);

      if (new_size > 0) {
        auto next_it = blocks.insert(std::next(block_it), {new_start, new_size, 0});
        free_blocks.emplace(new_size, next_it);
      }

      result.push_back(start);
    }
  }

  for (const int res : result) {
    std::cout << res << '\n';
  }
}