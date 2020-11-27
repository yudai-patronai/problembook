#include<vector>
#include<iostream>

enum class DfsState {
    kNotVisited,
    kInProgress,
    kVisited
};

int top_sort(const std::vector<std::vector<int>>& graph, int vertex, std::vector<DfsState>& visited, std::vector<int>& result) {
    if (visited[vertex] == DfsState::kInProgress) {
        return 1;
    }
    if (visited[vertex] == DfsState::kVisited) {
        return 0;
    }
    visited[vertex] = DfsState::kInProgress;
    for (auto i : graph[vertex]) {
        int error = top_sort(graph, i, visited, result);
        if (error != 0) {
            return error;
        }
    }
    visited[vertex] = DfsState::kVisited;
    result.push_back(vertex);
    return 0;
};

int main() {
    int V, E;
    std::cin >> V >> E;
    std::vector<std::vector<int>> graph(V);
    for (int i = 0; i < E; ++i) {
        int v, u;
        std::cin >> v >> u;
        graph[v].push_back(u);
    }
    std::vector<DfsState> visited(V, DfsState::kNotVisited);
    std::vector<int> result;
    for (int i = 0; i < V; ++i) {
        if (visited[i] == DfsState::kNotVisited) {
            int error = top_sort(graph, i, visited, result);
            if (error != 0) {
                std::cout << "NO" << std::endl;
                return 0;
            }
        }
    }
    for (auto it = result.rbegin(); it != result.rend(); ++it) {
        std::cout << *it << ' ';
    }
    std::cout << std::endl;
    return 0;
}
