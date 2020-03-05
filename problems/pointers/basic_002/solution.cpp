void my_personal_swap(int* a, int* b) {
    if (!a || !b)
        return;
    int tmp = *a;
    *a = *b;
    *b = tmp;
}
