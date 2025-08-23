from itertools import product
from pprint import pprint
from sys import stdin


def partition3_naive(values):
    for c in product(range(3), repeat=len(values)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(values[k] for k in range(len(values)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0

def partition3_faster(values):
    total = sum(values)
    if total % 3 != 0:
        return 0

    subset_size = total // 3
    n = len(values)
    dp_table = [[[0 for _ in range(subset_size + 1)]
                 for _ in range(subset_size + 1)]
                for _ in range(n + 1)]
    dp_table[0][0][0] = 1

    for i in range(1, n + 1):
        for j in range(subset_size + 1):
            for k in range(subset_size + 1):
                dp_table[i][j][k] = (dp_table[i-1][j][k] or
                                     (j-values[i-1] >= 0 and dp_table[i-1][j-values[i-1]][k]) or
                                     (k-values[i-1] >= 0 and dp_table[i-1][j][k-values[i-1]]))

    return int(dp_table[n][subset_size][subset_size])

def partition3(values):
    total = sum(values)
    if total % 3 != 0:
        return 0

    subset_size = total // 3
    n = len(values)
    dp_table = [[[[0 for _ in range(subset_size + 1)] for _ in range(subset_size +1)]
                for _ in range(subset_size + 1)] for _ in range(n + 1)]

    dp_table[0][0][0][0] = 1
    for i in range(1, n+1):
        for j in range(subset_size + 1):
            for k in range(subset_size + 1):
                for l in range(subset_size + 1):
                    dp_table[i][j][k][l] = ((j-values[i-1] >= 0 and dp_table[i-1][j-values[i-1]][k][l]) or
                            (k-values[i-1] >= 0 and dp_table[i-1][j][k-values[i-1]][l]) or
                            (l-values[i-1] >= 0 and dp_table[i-1][j][k][l-values[i-1]]))

    return int(dp_table[n][subset_size][subset_size][subset_size])


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3_faster(input_values))
