# python3


def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    dp_table =  [[float("inf") for _ in range(n+1)]
                 for _ in range(m+1)]
    dp_table[0][0] = 0

    for i in range(1, m+1):
        dp_table[i][0] = i

    for j in range(1, n+1):
        dp_table[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            substitution_cost = 0 if first_string[i-1] == second_string[j-1] else 1
            dp_table[i][j] = min(dp_table[i-1][j] + 1,
                                 dp_table[i][j-1] + 1,
                                 dp_table[i-1][j-1] + substitution_cost)

    return dp_table[m][n]



if __name__ == "__main__":
    print(edit_distance(input(), input()))
