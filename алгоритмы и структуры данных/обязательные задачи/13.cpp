#include <algorithm>
#include <array>
#include <climits>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

const std::array<int, 4> DirectionX = {-1, 0, 1, 0};
const std::array<int, 4> DirectionY = {0, 1, 0, -1};
const std::array<char, 4> DirectionChars = {'N', 'E', 'S', 'W'};

using Coord = std::pair<int, int>;
using State = std::pair<int, Coord>;

Coord ReadCoord() {
  int x, y;
  std::cin >> x >> y;
  return {x - 1, y - 1};
}

std::string RecreatePath(Coord start, Coord end, std::vector<std::vector<Coord>>& parent) {
  std::string path = "";
  int x = end.first, y = end.second;

  while (!(x == start.first && y == start.second)) {
    int px = parent[x][y].first;
    int py = parent[x][y].second;

    if (px == x - 1)
      path += 'S';
    else if (py == y + 1)
      path += 'W';
    else if (py == y - 1)
      path += 'E';
    else if (px == x + 1)
      path += 'N';

    x = px;
    y = py;
  }

  std::reverse(path.begin(), path.end());
  return path;
}

int main() {
  int n = 0, m = 0;
  std::cin >> n >> m;

  const Coord start = ReadCoord();
  const Coord end = ReadCoord();

  std::vector<std::vector<char>> matrix(n, std::vector<char>(m));
  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
      std::cin >> matrix[i][j];
    }
  }

  std::vector<std::vector<int>> dist(n, std::vector<int>(m, INT_MAX));
  std::vector<std::vector<Coord>> parent(n, std::vector<Coord>(m, {-1, -1}));
  std::priority_queue<State, std::vector<State>, std::greater<State>> pq;

  dist[start.first][start.second] = 0;
  pq.push({0, start});

  while (!pq.empty()) {
    const auto [cost, pos] = pq.top();
    pq.pop();

    if (pos == end)
      break;

    if (cost > dist[pos.first][pos.second])
      continue;

    for (int i = 0; i < 4; i++) {
      const Coord next = {pos.first + DirectionX[i], pos.second + DirectionY[i]};

      if (next.first < 0 || next.second < 0 || next.first >= n || next.second >= m)
        continue;

      if (matrix[next.first][next.second] == '#')
        continue;

      const int new_cost = cost + (matrix[next.first][next.second] == 'W' ? 2 : 1);

      if (new_cost < dist[next.first][next.second]) {
        dist[next.first][next.second] = new_cost;
        parent[next.first][next.second] = pos;
        pq.push({new_cost, next});
      }
    }
  }

  if (dist[end.first][end.second] == INT_MAX) {
    std::cout << -1;
  } else {
    std::cout << dist[end.first][end.second] << "\n";
    std::cout << RecreatePath(start, end, parent);
  }
}