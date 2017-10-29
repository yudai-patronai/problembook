#include <iostream>
#include <queue>
#include <map>
#include <vector>

void bfs_dist(std::map<int, std::vector<int>> &graph, int n)
{
    std::vector<int> dist;
    dist.reserve(n);
    for(int i = 0; i < n; ++i)
        dist[i] = -1;

    dist[0] = 0;
   
    std::queue<int> que;
    que.push(0);

    while (!que.empty())
    {
        int v = que.front();
        que.pop();

        for(auto v2 = graph[v].begin(); v2 != graph[v].end(); ++v2)
        {
            if (dist[*v2] == -1)
            {
                dist[*v2] = dist[v] + 1;
                que.push(*v2);
            }
        }
    }

    for(int i = 0; i < n; ++i)
        std::cout << dist[i] << std::endl;

    return;
}

int main()
{
    int n;
    int m;
    std::map<int, std::vector<int>> graph;

    std::cin >> n >> m;

    for(int i = 0; i < m; ++i)
    {
        int a, b;
        std::cin >> a >> b;
        graph[a].push_back(b);
        graph[b].push_back(a);
    }

    bfs_dist(graph, n);

    return 0;
}