#include <iostream>
#include <queue>
#include <vector>

int main() {
  int n = 0;
  std::cin >> n;

  std::vector<std::vector<int>> connections(n + 1);

  for (int i = 1; i <= n; ++i) {
    int u = 0;
    std::cin >> u;

    connections[i].push_back(u);
    connections[u].push_back(i);
  }

  std::vector<bool> visited(n + 1, false);
  int component_count = 0;

  for (int i = 1; i <= n; i++) {
    if (!visited[i]) {
      component_count++;
      std::queue<int> bfs_queue;
      bfs_queue.push(i);

      while (!bfs_queue.empty()) {
        const int next = bfs_queue.front();
        bfs_queue.pop();

        for (const int j : connections[next]) {
          if (!visited[j]) {
            visited[j] = true;
            bfs_queue.push(j);
          }
        }
      }
    }
  }

  std::cout << component_count;
}