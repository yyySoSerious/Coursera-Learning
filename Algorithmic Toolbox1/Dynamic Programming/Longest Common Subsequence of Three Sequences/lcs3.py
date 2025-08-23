# python3


def lcs3(first_sequence, second_sequence, third_sequence):
    m = len(first_sequence)
    n = len(second_sequence)
    o = len(third_sequence)

    dp_table = [[[0 for _ in range(o+1)]
                for _ in range(n + 1)]
                for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if first_sequence[i-1] == second_sequence[j-1] == third_sequence[k-1]:
                    dp_table[i][j][k] = dp_table[i-1][j-1][k-1] + 1
                else:
                    dp_table[i][j][k] = max(dp_table[i-1][j][k],
                                            dp_table[i][j-1][k],
                                            dp_table[i][j][k-1])

    return dp_table[m][n][o]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
