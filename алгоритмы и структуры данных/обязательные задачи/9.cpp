#include <iostream>
#include <queue>
#include <set>
#include <utility>
#include <vector>

int main() {
  int n = 0;
  int k = 0;
  int p = 0;
  int operations = 0;
  std::cin >> n >> k >> p;

  std::vector<int> cars(p);
  std::vector<std::queue<int>> paths(n);

  for (int i = 0; i < static_cast<int>(cars.size()); i++) {
    std::cin >> cars[i];
    paths[cars[i] - 1].push(i);
  }

  std::set<std::pair<int, int>> current_cars;
  for (const int car : cars) {
    const int last_use = paths[car - 1].front();
    paths[car - 1].pop();
    const int next_use = paths[car - 1].empty() ? p : paths[car - 1].front();

    if (static_cast<int>(current_cars.size()) < k && current_cars.count({last_use, car}) == 0) {
      current_cars.insert({next_use, car});
      operations += 1;
      continue;
    }

    if (current_cars.count({last_use, car}) != 0) {
      current_cars.erase({last_use, car});
      current_cars.insert({next_use, car});
      continue;
    }

    if (static_cast<int>(current_cars.size()) == k && current_cars.count({last_use, car}) == 0) {
      auto to_remove = --current_cars.end();
      current_cars.erase(to_remove);
      current_cars.insert({next_use, car});
      operations += 1;
    }
  }

  std::cout << operations;
}