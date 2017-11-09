#include <iostream>
#include <queue>
#include <vector>
#include <map>

int bfs_dist(std::map<int, std::vector<int>> &graph, int n, int x, int y)
{
    if (x == y)
        return 0;

    std::vector<int> dist;
    dist.reserve(n);
    for(int i = 0; i < n; ++i)
    	dist[i] = -1;
    dist[x] = 0;
   
    std::queue<int> que;
    que.push(x);

    while (!que.empty())
    {
        int v = que.front();
        que.pop();

        for(auto v2 = graph[v].begin(); v2 != graph[v].end(); ++v2)
        {
            if (dist[*v2] == -1)
            {
                dist[*v2] = dist[v] + 1;
                if (*v2 == y)
                    return dist[*v2];

                que.push(*v2);
            }
        }
    }

    return -1;
}

int main()
{
	int n;
	int m;
	int x,y;
	std::map<int, std::vector<int>> graph;

	std::cin >> n >> m >> x >> y;

	for(int i = 0; i < m; ++i)
	{
		int a, b;
		std::cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);

	}

	std::cout << bfs_dist(graph, n, x, y) << std::endl;

	return 0;
}