# python3

from random import randint

def partition33(array, left, right):
    pivot = array[left]
    s = left
    t = right
    i = left + 1
    while i <= t:
        if array[i] < pivot:
            array[i], array[s] = array[s], array[i]
            s += 1
            i += 1
        elif array[i] > pivot:
            array[i], array[t] = array[t], array[i]
            t -= 1
        else:
            i += 1

    return s, t

def partition3(array, left, right):
    pivot = array[left]
    s, t = left, left
    for i in range(left+1, right +1):
        if array[i] <= pivot:
            array[i], array[t] = array[t], array[i]
            t += 1
    for i in range(left, right+1):
        if array[i] < pivot:
            array[i], array[s] = array[s], array[i]
            s += 1
    return s, t-1


def randomized_quick_sort(array, left, right):
   while left < right:
        k = randint(left, right)
        array[left], array[k] = array[k], array[left]
        m, n = partition3(array, left, right)
        if m-left-1 < right - n-1:
            randomized_quick_sort(array, left, m-1)
            left = n +1
        else:
            randomized_quick_sort(array, n+1, right)
            right = m -1


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)
