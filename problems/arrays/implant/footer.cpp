

int main() {
    int L;
    cin >> L;
    int* mindstream = new int[L];
    for (int i = 0; i < L; i++)
        cin >> mindstream[i];
    int command = -1;
    int* frame = mindstream;
    int* end = mindstream + L;
    while (command) {
        recognize(frame, end, &command, &frame);
        if (!command) break;
        switch (command) {
            case 1:
                cout << "left ";
                break;
            case 2:
                cout << "right ";
                break;
            case 3:
                cout << "back ";
                break;
            case 4:
                cout << "MEOOOOW ";
                break;
        }
        frame += N;
    }
    cout << endl;
    delete[] mindstream;
    return 0;
}
