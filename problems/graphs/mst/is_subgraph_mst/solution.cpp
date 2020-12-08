#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

class DSU {
public:
    DSU() : par(0), sz(0), n(0) {}
    explicit DSU(size_t s) : par(s), sz(s), n(s) {
        for (size_t i = 0; i < s; ++i) {
            par[i] = i;
            sz[i] = 1;
        }
    }
    
    size_t get(size_t x) {
        size_t xb = x, xc;
        
        while (x != par[x]) {
            x = par[x];
        }
        
        while (xb != x) {
            xc = par[xb];
            par[xb] = x;
            xb = xc;
        }
        
        return x;
    }
    
    size_t add() {
        par.push_back(n);
        sz.push_back(1);
        return n++;
    }
    
    void merge(size_t x, size_t y) {
        x = get(x);
        y = get(y);
        if (sz[x] < sz[y]) {
            std::swap(x, y);
        }
        
        par[y] = x;
        sz[x] += sz[y];
    }
    
    bool same(size_t x, size_t y) {
        return (get(x) == get(y));
    }
    
private:
    std::vector<size_t> par, sz;
    size_t n;
};

struct Edge {
    size_t from, to;
    int64_t weight;
    
    Edge(size_t f, size_t t, int64_t w) : from(f), to(t), weight(w) {}
    
    bool operator<(const Edge& rhs) const {
        return weight < rhs.weight;
    }
    
    bool operator>(const Edge& rhs) const {
        return weight > rhs.weight;
    }
};

int NO() {
    std::cout << "NO\n";
    return 0;
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    size_t n, m;
    std::cin >> n >> m;
    
    std::vector<Edge> edges;
    edges.reserve(m);
    
    size_t f, t;
    int64_t w;
    
    for (size_t i = 0; i < m; ++i) {
        std::cin >> f >> t >> w;
        --f; --t;
        edges.emplace_back(f, t, w);
    }
    
    int64_t mst_weight = 0;
    
    {
        std::priority_queue<Edge, std::vector<Edge>, std::greater<Edge>> q(std::greater<Edge>{}, std::vector<Edge>(edges));
        DSU d(n);
        size_t unseen = n - 1;
        
        while ((unseen > 0) && (!q.empty())) {
            const Edge& e = q.top();
            if (d.get(e.from) != d.get(e.to)) {
                mst_weight += e.weight;
                d.merge(e.from, e.to);
                --unseen;
            }
            q.pop();
        }
        
        if (unseen > 0) {
            return NO();
        }
    }
        
    size_t k;
    std::cin >> k;
    
    if (k != n - 1) {
        return NO();
    }
    
    DSU d(n);
    int64_t measured_weight = 0;
    
    size_t ix;
    for (size_t i = 0; i < k; ++i) {
        std::cin >> ix;
        --ix;
        const Edge& e = edges[ix];
        
        if (d.get(e.from) == d.get(e.to)) {
            return NO();
        }
        d.merge(e.from, e.to);
        
        measured_weight += e.weight;
    }
    
    if (measured_weight > mst_weight) {
        return NO();
    }
    
    if (measured_weight < mst_weight) {
        std::cout << "Logic error\n";
        return 1;
    }
    
    std::cout << "YES\n";
    return 0;
}
