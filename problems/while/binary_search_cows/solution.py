"""
https://informatics.msk.ru/mod/statements/view3.php?id=1966&chapterid=1

На прямой расположены стойла, в которые необходимо расставить коров так, чтобы минимальное расcтояние между коровами было как можно больше.
Входные данные

В первой строке вводятся числа N  (2 < N < 10001) – количество стойл и K  (1 < K < N ) – количество коров. Во второй строке задаются N натуральных чисел в порядке возрастания – координаты стойл (координаты не превосходят 109)
Выходные данные

Выведите одно число – наибольшее возможное допустимое расстояние.
"""

def can_place(A, d, K):
    # проверяет, можно ли расставить K коров по стойлам с координатами А так,
    # чтобы расстояние между ними было не меньше d
    count = 1

    j = 0 # куда поставили предыдущую корову
    for i in range(1, len(A)):
        if A[i] - A[j] >= d:
            j = i
            count += 1
        
        if count == K:
            return True
    
    return False


def bin_search(A, K):
    left = 1                #  левая граница расстояний
    right =  A[-1] - A[0]   # правая граница расстояний
    # ищем границу по расстоянию, где can_place меняет значение c True на False
    while left < right:
        m = (left + right) // 2

        canl = can_place(A, m-1, K)
        can = can_place(A, m, K)
        canr = can_place(A, m+1, K)

        if can and not canr:
            answer = m
            break

        if canl and not can:
            answer = m - 1
            break

        if not can:
            right = m - 1
        else:
            left = m + 1
    
    return answer


def linear_search(A, K):
    # для тестирования времени, похоже на массиве A = 0..10000 уже существенно медленней
    left = 1
    right =  A[-1] - A[0]
    for i in range(left, right+1):
        if can_place(A, i, K) and not can_place(A, i+1, K):
            return i

N, K = map(int, input().split())
A = list(map(int, input().split()))

print(bin_search(A, K))

# тест на время
# A = list(range(10001))
# print(bin_search(A, 3))    # < 0.1 sec
# print(linear_search(A, 3)) # 7 sec

