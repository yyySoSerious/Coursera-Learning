# python3


def find_maximum_value(dataset):
    digits = dataset[::2]
    operations = dataset[1::2]
    n = len(digits)
    dp_max = [[float("-inf")] * n for _ in range(n)]
    dp_min = [[float("inf") ]* n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = int(digits[i])
        dp_min[i][i] = int(digits[i])

    for length in range(1, n):
        for i in range(n-length):
            j = i + length
            for k in range(i, j):
                if operations[k] == "+":
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                elif operations[k] == "-":
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])
                elif operations[k] == "*":
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] * dp_max[k + 1][j],
                                       dp_max[i][k] * dp_min[k + 1][j],
                                       dp_min[i][k] * dp_min[k + 1][j],
                                       dp_min[i][k] * dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j],  dp_max[i][k] * dp_max[k + 1][j],
                                       dp_max[i][k] * dp_min[k + 1][j],
                                       dp_min[i][k] * dp_min[k + 1][j],
                                       dp_min[i][k] * dp_max[k + 1][j])

    return dp_max[0][n-1]

if __name__ == "__main__":
    print(find_maximum_value(input()))
