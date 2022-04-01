struct GCP {
    uint32_t *c;
    bool *r;
    size_t n;

    GCP(size_t n_) : n(n_) {
        c = new uint32_t[n];
        r = new bool[n];

        for (size_t i = 0; i < n; ++i) {
            c[i] = 0;
            r[i] = false;
        }
    }

    uint32_t operator[](size_t i) {
        i += n;
        i %= n;

        if (!r[i]) {
            r[i] = true;
            c[i] = get_results(i);
        }

        return c[i];
    }

    ~GCP() {
        delete[] r;
        delete[] c;
    }
};

size_t GetBound(GCP& g, size_t base) {
    if (g.r[base]) return base;
    if (g.r[base - 1]) return base - 1;
    if (g.r[base + 1]) return base + 1;
    return base;
}

size_t Find2(GCP& g, size_t l, size_t r) {
    auto mi = l;
    auto mv = g[l];

    for (auto i = l + 1; i <= r; ++i) {
        if (g[i] > mv) {
            mv = g[i];
            mi = i;
        }
    }
    return mi;
}

size_t Find1(GCP& g, size_t l, size_t r) {
    // std::cerr << "Find1 (" << l << ";" << r << ")\n";

    if (r - l < 4) {
        return Find2(g, l, r);
    }

    size_t step = round((r - l)/4.0);
    size_t bnd[5] {l, l + step, l + 2 * step, l + 3 * step, r};

    if (step >= 3) {
        for (size_t i = 1; i < 4; ++i) bnd[i] = GetBound(g, bnd[i]);
    }

    size_t i = 0;

    while (g[bnd[i]] > g[bnd[i + 1]]) {
        ++i;
        if (i == 4) {
            return Find1(g, l, bnd[1]);
        }
    }

    while (g[bnd[i]] < g[bnd[i + 1]]) {
        ++i;
        if (i == 4) {
            return Find1(g, bnd[3], r);
        }
    }


    if (i == 0) {
        std::cerr << "How this even happened?\n";
        return Find1(g, l + g.n - step, l + g.n + step);
    }

    return Find1(g, bnd[i - 1], bnd[i + 1]);
}


void detect() {
    GCP g(360);
    auto ix = Find1(g, 0, 359);
    std::cout << g[ix] << " " << ix << "\n";
}
