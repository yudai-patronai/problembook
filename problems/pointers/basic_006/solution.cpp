unsigned int count_total_mice_amount(Cat* cats, unsigned int n) {
    if (!cats)
        return 0;
    unsigned int res = 0;
    for (unsigned int i = 0; i < n; i++)
        res += cats[i].mice_caught;
    return res;
}
