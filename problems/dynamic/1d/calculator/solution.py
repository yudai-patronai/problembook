# https://informatics.mccme.ru/mod/statements/view.php?id=654&chapterid=2963
#
# Имеется калькулятор, который выполняет три операции:
#     Прибавить к числу X единицу.
#      Умножить число X на 2.
#     Умножить число X на 3.
#
# Определите, какое наименьшее число операций необходимо для того, чтобы получить из числа 1 заданное число N.
#
# Входные данные
# Программа получает на вход одно число, не превосходящее 10^6.
# Выходные данные
# Требуется вывести одно число: наименьшее количество искомых операций.


def solution(N):
    if N == 1:
        return 0
    if N == 2:
        return 2
    if N == 3:
        return 3
    
    methods = [None] * (N + 1)
    methods[1] = 0
    methods[2] = 1
    methods[3] = 1

    for i in range(4, N+1):
        methods[i] = methods[i-1] + 1
        if i % 2 == 0:
            methods[i] = min(methods[i], methods[i//2] + 1)
        if i % 3 == 0: 
            methods[i] = min(methods[i], methods[i//3] + 1)
    return methods[N]


N = int(input())
print(solution(N))
