struct TableFunction final {
    TableFunction(std::vector<ArgVal> const &table): table(table) { }

    double operator()(double x) const {
        auto it = std::find_if(table.begin(),table.end(),[&x](ArgVal p) { return p.first >= x;});
        if (it == table.begin()) return table.front().second;
        if (it == table.end()) return table.back().second;
        return interpolate(*it,*prev(it),x); 
    }

private:
    std::vector<ArgVal> const table;
};