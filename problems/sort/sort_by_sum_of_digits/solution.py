# encoding: utf-8


def get_sum_of_digits(number):

    sum_of_digits = 0
    while number > 0:
        sum_of_digits += number % 10
        number //= 10

    return sum_of_digits


def modified_bubble_sort(array, sort_by_array):

    for i in range(len(sort_by_array)):
        for j in range(i, len(sort_by_array)):
            if sort_by_array[i] > sort_by_array[j] or sort_by_array[i] == sort_by_array[j] and array[i] > array[j]:
                sort_by_array[i], sort_by_array[j] = sort_by_array[j], sort_by_array[i]
                array[i], array[j] = array[j], array[i]

    return array


def sort_by_sum(array):

    digits_sum_array = [0] * len(array)

    for i in range(len(array)):
        digits_sum_array[i] = get_sum_of_digits(array[i])

    return modified_bubble_sort(array, digits_sum_array)


if __name__ == '__main__':

    N = int(input())
    array = []

    for _ in range(N):
         array.append(int(input()))

    ans = sort_by_sum(array)

    for i in ans:
        print(i)
