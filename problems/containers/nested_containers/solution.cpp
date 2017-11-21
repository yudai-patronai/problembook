#include<iostream>
#include<map>
#include<vector>

int main() {
    std::map<int, std::vector<int>> vertices;

    unsigned edge_count;
    std::cin >> edge_count;

    for (unsigned i = 0; i < edge_count; ++i) {
        unsigned source, destination;
        unsigned weight;

        std::cin >> source >> destination >> weight;
        vertices[source].push_back(weight);
    }

    for (auto& vertex : vertices) {
        unsigned weight = 0;
        for (auto& edge : vertex.second)
            weight += edge;
        std::cout << vertex.first << " "
            << vertex.second.size() << " "
            << weight << std::endl;
    }

    return 0;
}
