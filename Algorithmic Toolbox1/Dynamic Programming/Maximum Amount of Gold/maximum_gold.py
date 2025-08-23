# python3
from pprint import pprint
from sys import stdin


def maximum_gold(capacity, weights):
    m = capacity
    n = len(weights)
    dp_table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for curr_capacity in range(1, m + 1):
        for weight_idx in range(1, n + 1):
            curr_weight = weights[weight_idx-1]
            if curr_weight <= curr_capacity:
                remaining_capacity = curr_capacity - curr_weight
                dp_table[curr_capacity][weight_idx] = max(dp_table[remaining_capacity][weight_idx-1] + curr_weight,
                                                          dp_table[curr_capacity][weight_idx-1])
            else:
                dp_table[curr_capacity][weight_idx] = dp_table[curr_capacity][weight_idx-1]

    return dp_table[m][n]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
