void my_slightly_less_dumb_reallocation(int** source,
        unsigned int n_old, unsigned int n_new) {
    if (!source)
        return;
    if (!*source || !n_old) {
        *source = n_new ? new int[n_new] : NULL;
        return;
    }
    if (!n_new) {
        delete[] *source;
        *source = NULL;
        return;
    }
    int *out = new int[n_new];
    for (unsigned int i = 0; i < n_new && i < n_old; i++)
        out[i] = (*source)[i];
    delete[] *source;
    *source = out;
}

