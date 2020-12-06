#include <iostream>
#include <vector>
#include <set>

struct Graph {
    struct Edge {
        size_t from, to;
        Edge(size_t f, size_t t) : from(f), to(t) {}
    };
    size_t n;
    std::vector<std::vector<Edge>> edges;

    explicit Graph(size_t n_): n(n_), edges(n, std::vector<Edge>()) {}
    void AddEdge(size_t from, size_t to) {
        edges[from].emplace_back(from, to);
    }
};

struct APFinder {
    const Graph& g;
    std::vector<bool> used;
    std::vector<size_t> tin, fup;
    size_t timer;
    std::set<size_t> aps;

    struct DfsInfo {
        size_t i, to, node, parent;
    };

    size_t rchldnum = 0;

    explicit APFinder(const Graph& g_)
    : g(g_), used(g.n, false), tin(g.n, 0), fup(g.n, 0), timer(0), aps({})
    {}

    void Find() {
        DfsIt(0);
    }

    void DfsIt(size_t start) {
        // In fact it was probably easier to just modify the %rsp.
        // Well, never mind.

        std::vector<DfsInfo> stack;

        stack.push_back({0, g.n, start, g.n});

        size_t i, to, node, parent;

        while (! stack.empty()) {
            i = stack.back().i;
            to = stack.back().to;
            node = stack.back().node;
            parent = stack.back().parent;

            bool finished = true;

            if (to == g.n) {
                used[node] = true;
                tin[node] = timer;
                fup[node] = timer;
                ++timer;
                to = 0;
            } else {
                fup[node] = std::min(fup[node], fup[to]);
                if ((fup[to] >= tin[node]) && (parent != g.n)) {
                    aps.insert(node);
                }
                if (parent == g.n) ++rchldnum;
                ++i;
            }

            for (; i < g.edges[node].size(); ++i) {
                to = g.edges[node][i].to;
                if (to == parent) {
                    continue;
                }

                if (used[to]) {
                    fup[node] = std::min(fup[node], tin[to]);
                } else {
                    stack.back().i = i;
                    stack.back().to = to;

                    stack.push_back({0, g.n, to, node});
                    finished = false;
                    break;
                }
            }

            if ((parent == g.n) && (rchldnum > 1)) {
                aps.insert(node);
            }

            if (finished) {
                stack.pop_back();
            }
        }
    }

    void Dfs(size_t node, size_t parent) {
        used[node] = true;
        tin[node] = timer;
        fup[node] = timer;
        ++timer;

        for (size_t i = 0; i < g.edges[node].size(); ++i) {
            auto to = g.edges[node][i].to;
            if (to == parent) {
                continue;
            }

            if (used[to]) {
                fup[node] = std::min(fup[node], tin[to]);
            } else {
                Dfs(to, node);
                fup[node] = std::min(fup[node], fup[to]);
                if ((fup[to] >= tin[node]) && (parent != g.n)) {
                    aps.insert(node);
                }
                if (parent == g.n) ++rchldnum;
            }
        }

        if ((parent == g.n) && (rchldnum > 1)) {
            aps.insert(node);
        }
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    size_t n, m;
    std::cin >> n >> m;
    Graph g(n);

    {
        size_t f, t;
        for (size_t i = 0; i < m; ++i) {
            std::cin >> f >> t;
            --f; --t;
            g.AddEdge(f, t);
            g.AddEdge(t, f);
        }
    }

    APFinder f(g);
    f.Find();

    if (f.aps.empty()) {
        std::cout << "-1";
    } else {
        for (auto cand : f.aps) {
            std::cout << (cand + 1) << " ";
        }
    }
    std::cout << "\n";
}
