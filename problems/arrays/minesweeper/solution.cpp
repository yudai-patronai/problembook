#include <iostream>

int main() {
    int  N, M, X, Y, K;
    std::cin >> N;
    std::cin >> M;
    std::cin >> K;
    int **ptrArray = new int* [N];

    for (int count = 0; count < N; count++)
              ptrArray[count] = new int[M];

    for (int countX = 0; countX < N; countX++)
        for (int countY = 0; countY < M; countY++)
                ptrArray[countX][countY] = 0;

    for (int count = 0; count < K; count++) {
        std::cin >> X;
        std::cin >> Y;
        X--; Y--;
        ptrArray[X][Y] = -1;

        if ((X > 0) && (Y > 0) && (ptrArray[X-1][Y-1] != -1))
                ptrArray[X-1][Y-1]++;

        if ((X > 0) && (ptrArray[X-1][Y] != -1))
                ptrArray[X-1][Y]++;

        if ((X > 0) && (Y < M - 1) && (ptrArray[X-1][Y+1] != -1))
                ptrArray[X-1][Y+1]++;

        if ( (Y > 0) && (ptrArray[X][Y-1] != -1))
                ptrArray[X][Y-1]++;

        if ( (Y < M - 1) && (ptrArray[X][Y+1] != -1))
                ptrArray[X][Y+1]++;

        if ((X < N - 1) && (Y > 0) && (ptrArray[X+1][Y-1] != -1))
                ptrArray[X+1][Y-1]++;

        if ((X < N - 1) && (ptrArray[X+1][Y] != -1))
                ptrArray[X+1][Y]++;

        if ((X < N - 1) && (Y < M - 1) && (ptrArray[X+1][Y+1] != -1))
                ptrArray[X+1][Y+1]++;
    }

    for (int countX = 0; countX < N; countX++) {
        for (int countY = 0; countY < M; countY++) {
            std::cout << ptrArray[countX][countY] << " ";
        }
        std::cout << std::endl;
    }

    for (int count = 0; count < 2; count++)
              delete []ptrArray[count];

    delete [] ptrArray;
    return 0;
}
