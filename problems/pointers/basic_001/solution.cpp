int* now_get_me_some_bytes(unsigned int n) {
    return new int[n];
}

void now_free_some_bytes(int* p) {
    delete[] p;
}
