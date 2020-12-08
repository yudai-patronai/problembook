#include <iostream>
#include <vector>
#include <set>
#include <utility>

struct Graph {
    struct Edge {
        size_t from, to;
        int64_t weight;
        Edge(size_t f, size_t t, int64_t w) : from(f), to(t), weight(w) {}
    };
    size_t n;
    std::vector<std::vector<Edge>> edges;

    explicit Graph(size_t n_): n(n_), edges(n, std::vector<Edge>()) {}
    void AddEdge(size_t from, size_t to, int64_t weight) {
        edges[from].emplace_back(from, to, weight);
    }
};

struct BFinder {
    const Graph& g;
    std::vector<bool> used;
    std::vector<size_t> tin, fup;
    size_t timer;

    Graph::Edge cmin;

    struct DfsInfo {
        size_t i, to, node, parent;
        int64_t weight;
    };

    explicit BFinder(const Graph& g_)
    : g(g_), used(g.n, false), tin(g.n, 0), fup(g.n, 0),
      timer(0), cmin(g.n, g.n, -(1ll<<30))
    {}

    void Find() {
        DfsIt(0);
    }

    void DfsIt(size_t start) {
        // In fact it was probably easier to just modify the %rsp.
        // Well, never mind.

        std::vector<DfsInfo> stack;

        stack.push_back({0, g.n, start, g.n, -(1ll<<30)});

        size_t i, to, node, parent;

        while (!stack.empty()) {
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
                if (fup[to] > tin[node]) {
                    if (stack.back().weight > cmin.weight) {
                        cmin.weight = stack.back().weight;
                        cmin.from = node;
                        cmin.to = to;
                    }
                }
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
                    stack.back().weight = g.edges[node][i].weight;

                    stack.push_back({0, g.n, to, node,
                                     g.edges[node][i].weight});
                    finished = false;
                    break;
                }
            }

            if (finished) {
                stack.pop_back();
            }
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
        int64_t w;
        for (size_t i = 0; i < m; ++i) {
            std::cin >> f >> t >> w;
            --f; --t;
            g.AddEdge(f, t, w);
            g.AddEdge(t, f, w);
        }
    }

    BFinder f(g);
    f.Find();

    if (f.cmin.from == g.n) {
        std::cout << "-1";
    } else {
        std::cout << f.cmin.weight;
        /*if (f.cmin.from <= f.cmin.to) {
            std::cout << (f.cmin.from + 1) << " " << (f.cmin.to + 1) << " " << f.cmin.weight;
        } else {
            std::cout << (f.cmin.to + 1) << " " << (f.cmin.from + 1) << " " << f.cmin.weight;
        }*/
    }
    std::cout << "\n";
}
