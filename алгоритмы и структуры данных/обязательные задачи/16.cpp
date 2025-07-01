#include <algorithm>
#include <iostream>
#include <stack>
#include <vector>

bool static DFS(int distance, const std::vector<std::vector<int>>& matrix, int n, bool revers) {
  std::vector<bool> visited(n, false);

  std::stack<int> dfs_stack;
  dfs_stack.push(0);
  visited[0] = true;

  while (!dfs_stack.empty()) {
    const int i = dfs_stack.top();
    dfs_stack.pop();

    for (int j = n - 1; j >= 0; j--) {
      if (!revers && !visited[j] && matrix[i][j] <= distance) {
        visited[j] = true;
        dfs_stack.push(j);
      }

      if (revers && !visited[j] && matrix[j][i] <= distance) {
        visited[j] = true;
        dfs_stack.push(j);
      }
    }
  }

  for (int i = 0; i < n; i++) {
    if (!visited[i]) {
      return false;
    }
  }

  return true;
}

bool static IsConnected(int distance, const std::vector<std::vector<int>>& matrix, int n) {
  return DFS(distance, matrix, n, false) && DFS(distance, matrix, n, true);
}

int main() {
  int n = 0;
  int high = 0;
  int low = 0;

  std::cin >> n;

  std::vector<std::vector<int>> matrix(n, std::vector<int>(n, 0));

  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      std::cin >> matrix[i][j];
      high = std::max(high, matrix[i][j]);
    }
  }

  while (high - 1 > low) {
    const int mid = low + ((high - low) / 2);

    if (IsConnected(mid, matrix, n)) {
      high = mid;
    } else {
      low = mid;
    }
  }

  std::cout << high;
}
