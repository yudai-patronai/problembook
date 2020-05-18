Move* counterwise_repair(Move* arr_, int N_)
{
    long int kol = 1;
    long int i;
    for (i = 1; i < N_; i++){
        kol = 3*kol+1;
    }
    Move *counterarr = new Move[kol];
    for(long int i = 0; i < kol; i++){
        counterarr[i].num = arr_[kol-i-1].num;
        counterarr[i].from = arr_[kol-i-1].to;
        counterarr[i].to = arr_[kol-i-1].from;
    }
    return counterarr;
}

Move* repair(Move* arr_, int N_) {
    long int kol = 1;
    long int n;
    for (n = 1; n < N_; n++){
        kol = 3*kol+1;
    }
    Move *smallarr = new Move[kol];
    for(long int n = 0; n < kol; n++){
        smallarr[n].num = arr_[n].num;
        if (arr_[n].to == 2) {
            smallarr[n].to = 3;
        }
        else {
            if (arr_[n].to == 3) {
                smallarr[n].to = 2;
            }
            else {
                smallarr[n].to = 1;
            }
        }
        if (arr_[n].from == 2) {
            smallarr[n].from = 3;
        }
        else {
            if (arr_[n].from == 3) {
                smallarr[n].from = 2;
            }
            else {
                smallarr[n].from = 1;
            }
        }
    }
    return smallarr;
}

Move* hanoi_repair(int N)
{
    long int kol = 1;
    long int i;
    for (i = 1; i < N; i++){
        kol = 3*kol+1;
    }
    Move* arr = new Move[kol+1];
    if (kol == 1) {
        arr[0].num = 1;
        arr[0].from = 1;
        arr[0].to = 3;
    }
    else {
        Move* sarr = repair(hanoi_repair(N-1), N-1);
        for (i = 0; i < kol/3; i++)
        {
            arr[i]= sarr[i];
        }
        delete sarr;
        arr[kol/3].num = N;
        arr[kol/3].from = 1;
        arr[kol/3].to = 3;
        sarr = counterwise_repair(repair(hanoi_repair(N-1), N-1),N-1);
        for (i = kol/3+1; i < 2*(kol/3)+1; i++)
        {
            arr[i] = sarr[i - kol/3 - 1];
        }
        delete sarr;
        sarr = hanoi_repair(N-1);
        for (i = 2*(kol/3)+1; i < kol; i++)
        {
            arr[i] = sarr[i - 2*(kol/3) - 1];
        }
        delete sarr;
    }
    arr[kol].num = 5;
    arr[kol].from = 5;
    arr[kol].to = 5;
    return arr;
}

