int* my_slightly_dumb_reallocation(int* source,
        unsigned int n_old, unsigned int n_new) {
    if (!source || !n_old) {
        return n_new ? new int[n_new] : NULL;
    }
    if (!n_new) {
        delete[] source;
        return NULL;
    }
    int *out = new int[n_new];
    for (unsigned int i = 0; i < n_new && i < n_old; i++)
        out[i] = source[i];
    delete[] source;
    return out;
}
