bool check_move(int num, int from, int to, int N, int* mass)
{
    int i;
    for (i = 0; i < num - 1; i++) //проверяем, что нет более лёгких там "куда"
    {
        if (mass[i] == to) {
                return false;
        }
    }
    if ((from == 2) && (to == 3)) {
            return false; //ремонт как бы
    }
    for (i = 0; i < num - 1; i++) //проверяем, что нет более лёгких там "откуда"
    {
        if (mass[i] == from) {
                return false;
        }
    }
    return true;
}

int correct_check(int N, Move* arr)
{
    int mass[10];
    int flag = 1;
    long int i;
    for(i = 0; i < N; i++){
        mass[i] = 1;
    }
    i = 0;
    while (arr[i].from != 5){
        i++;
    }
    long int k = i;
    if (k > 200000){
        flag = 0;
        return flag;
    }
    for (i = 0; i < k; i++){
        if (check_move(arr[i].num, arr[i].from, arr[i].to, N, mass)){
            mass[arr[i].num- 1] = arr[i].to;
        }
        else {
            flag = 0;
            return flag;
        }
    }
    for (i = 0; i < N; i++){
        if (mass[i] != 3){
            flag = 0;
            return flag;
       }
    }
    return flag;
}

int main()
{
    Move* arr_;
    int i = 0;
    int N_;
    std::cin >> N_;
    arr_ = hanoi_repair(N_); //функция студентов
    if (correct_check(N_, arr_) == 1) {
        std::cout << "YES";
    }
    else {
        std::cout << "NO";
    }
    delete arr_;
    return 0;
} 
