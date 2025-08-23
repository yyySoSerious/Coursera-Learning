# python3

from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def merge_and_count_inversions(a, b):
    c = []
    i, j = 0, 0
    num_inversions = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            num_inversions += (len(a) - i)
    c.extend(a[i:])
    c.extend(b[j:])
    return c, num_inversions

def sort_and_count_inversions(a):
    if len(a) == 1:
        return a, 0
    middle = len(a)//2
    left, left_inversions = sort_and_count_inversions(a[:middle])
    right, right_inversions = sort_and_count_inversions(a[middle:])

    final, agg_inversions = merge_and_count_inversions(left, right)
    num_inversions = agg_inversions + left_inversions + right_inversions
    return final, num_inversions

def compute_inversions(a):
    _, num_inversions = sort_and_count_inversions(a)
    return num_inversions

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(compute_inversions(elements))
