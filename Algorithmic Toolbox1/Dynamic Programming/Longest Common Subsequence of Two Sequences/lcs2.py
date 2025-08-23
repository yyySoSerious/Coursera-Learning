# python3


def lcs2_two(first_sequence, second_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    dp_table = [[0 for _ in range(n+1)]
                for _ in range(m+1)]

    for i in range(1, m + 1):
        for j in range(1, n +1):
            if first_sequence[i-1] == second_sequence[j-1]:
                dp_table[i][j] = dp_table[i-1][j-1] + 1
            else:
                dp_table[i][j] = max(dp_table[i-1][j], dp_table[i][j-1])

    return dp_table[m][n]

def lcs2(first_sequence, second_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    dp_table = [[float("inf") for _ in range(n + 1)]
                for _ in range(m + 1)]
    dp_table[0][0] = 0

    for i in range(1, m + 1):
        dp_table[i][0] = i

    for j in range(1, n + 1):
        dp_table[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            operation_cost = dp_table[i-1][j-1] if first_sequence[i-1] == second_sequence[j-1] else float("inf")
            dp_table[i][j] = min(dp_table[i-1][j] + 1,
                                 dp_table[i][j-1] + 1,
                                 operation_cost)

    length = 0
    i = m
    j = n
    while i > 0 and j > 0:
        operation_cost  = 0 if first_sequence[i-1] == second_sequence[j-1] else -1
        prev_operation = dp_table[i][j] + operation_cost
        if dp_table[i-1][j] == prev_operation:
            i -= 1
        elif dp_table[i][j-1] == prev_operation:
            j -= 1
        elif dp_table[i-1][j-1] == prev_operation:
            i -= 1
            j -= 1
            length += 1
        else:
            raise ValueError(f"Error: dp_table at this index expects prev operation to have used {prev_operation} number of operations")
    return length


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
