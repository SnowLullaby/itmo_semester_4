#include <iostream>
#include <stack>
#include <utility>
#include <vector>

bool static DFS(
    int start, const std::vector<std::vector<int>>& connections, std::vector<int>& colors
) {
  std::stack<std::pair<int, int>> dfs_stack;
  dfs_stack.emplace(start, 0);
  colors[start] = 0;

  while (!dfs_stack.empty()) {
    auto [next, color] = dfs_stack.top();
    dfs_stack.pop();

    for (const int j : connections[next]) {
      if (colors[j] == -1) {
        colors[j] = 1 - color;
        dfs_stack.emplace(j, colors[j]);
      }

      if (colors[j] == colors[next]) {
        return false;
      }
    }
  }

  return true;
}

int main() {
  int n = 0;
  int m = 0;
  std::cin >> n >> m;

  std::vector<std::vector<int>> connections(n + 1);

  for (int i = 0; i < m; ++i) {
    int u = 0;
    int v = 0;
    std::cin >> u >> v;
    connections[u].push_back(v);
    connections[v].push_back(u);
  }

  std::vector<int> colors(n + 1, -1);
  bool res = true;

  for (int i = 1; i <= n; i++) {
    if (colors[i] == -1) {
      if (!DFS(i, connections, colors)) {
        res = false;
        break;
      }
    }
  }

  if (res) {
    std::cout << "YES";
  } else {
    std::cout << "NO";
  }
}