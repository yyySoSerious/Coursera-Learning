# python3


def compute_optimal_summands(n):
    assert 1 <= n <= 10 ** 9
    summands = []
    leftover = n
    i = 1
    while True:
        if leftover == 0:
            break
        if 0 < (leftover - i) <= i:
            i += 1
            continue
        leftover -= i
        summands.append(i)
        i += 1

    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
