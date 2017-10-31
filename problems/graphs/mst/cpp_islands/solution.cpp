#include <iostream>
#include <map>
#include <vector>
#include <utility>

int solve(int n, const std::vector<std::pair<int, int>>& edges) {
    std::vector<int> comp;
    for (int i = 0; i < n; i++)
        comp.push_back(i);

    int n_comp = n;
    std::vector<std::vector<int>> components;
    for (int i = 0; i < n_comp; i++) {
        components.push_back(std::vector<int>());
        components[i].push_back(i);
    }

    for (unsigned i = 0; i < edges.size(); i++) {
        auto& edge = edges[i];
        int a = comp[edge.first], b = comp[edge.second];

        if (a != b) {
            n_comp--;
            if (n_comp == 1)
                return i + 1;
            if (components[a].size() < components[b].size())
                std::swap(a, b);

            for (auto v : components[b])
                comp[v] = a;

            components[a].insert(
                components[a].end(),
                components[b].begin(),
                components[b].end());
            components[b] = std::vector<int>();
        }
    }

    return edges.size();
}


int main() {
    int n, m;
    std::cin >> n >> m;

    std::vector<std::pair<int, int>> edges;
    edges.reserve(m);

    for (int i = 0; i < m; i++) {
        int from, to;
        std::cin >> from >> to;
        edges.push_back(std::make_pair(from, to));
    }

    std::cout << solve(n, edges) << std::endl;

    return 0;
}
