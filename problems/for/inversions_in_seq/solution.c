#include <stdio.h>

int main()
{
    int x, prev;
    int n = 0;
    scanf("%d", &prev);
    scanf("%d", &x);
    while (x != 0)
    {
        if (prev < x)
            n += 1;
        prev = x;
        scanf("%d", &x);
    }

    printf("%d\n", n);
    return 0;
}

