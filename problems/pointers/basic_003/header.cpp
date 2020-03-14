int do_some_awesome_work(int* a, int* b) {
    int _a = *a, _b = *b;
    if (_a > 0) return _a;
    if (_b < 0) return _b;
    return _a + _b > 10 ? _a * _b : _a % _b;
}
