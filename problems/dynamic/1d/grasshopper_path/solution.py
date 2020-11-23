# https://informatics.mccme.ru/mod/statements/view.php?id=654&chapterid=915
#
# Мальчик подошел к платной лестнице.
# Чтобы наступить на любую ступеньку, нужно заплатить указанную на ней сумму.
# Мальчик умеет перешагивать на следующую ступеньку, либо перепрыгивать через ступеньку.
# Требуется узнать, какая наименьшая сумма понадобится мальчику, чтобы добраться до верхней ступеньки.
#
# Входные данные
# В первой строке входного файла вводится одно натуральное число N ≤ 100 — количество ступенек.
# В следующей строке вводятся 𝑁 натуральных чисел, не превосходящих 100 — стоимость каждой ступеньки (снизу вверх).

def solution(N, costs):
    min_sum = [101] * N  # 101 - max cost
    min_sum[0] = costs[0]
    min_sum[1] = costs[1]  # costs[i] >= 1
    for i in range(2, N):
        min_sum[i] = costs[i] + min(min_sum[i-1], min_sum[i-2])

    # recover path
    i = N-1
    path = []
    while i > -1:
        path.append(i)
        if min_sum[i] == min_sum[i-1] + costs[i]:
            i -= 1
        elif min_sum[i] == min_sum[i-2] + costs[i]:
            i -= 2
        else:
            break

    return min_sum[N-1], path[::-1]


if __name__ == "__main__":
    N = int(input())
    costs = list(map(int, input().split()))

    m, path = solution(N, costs)

    print(m)
    print(*path)
