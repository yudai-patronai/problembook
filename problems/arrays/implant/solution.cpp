bool check(int* data, const int* pattern) {
    for (size_t j = 0; j < N; j++)
        if (data[j] != pattern[j])
            return false;
    return true;
}

void recognize(int* data_start, int* data_end, int* command, int** frame) {
    while (data_end - data_start >= N) {
        if (check(data_start, left)) {
            *command = 1;
            *frame = data_start;
            return;
        }
        if (check(data_start, right)) {
            *command = 2;
            *frame = data_start;
            return;
        }
        if (check(data_start, back)) {
            *command = 3;
            *frame = data_start;
            return;
        }
        if (check(data_start, meow)) {
            *command = 4;
            *frame = data_start;
            return;
        }
        data_start++;
    }

    *command = 0;
    *frame = nullptr;
}
