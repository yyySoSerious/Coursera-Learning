# python3


def fibonacci_number_again_naive(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3

    if n <= 1:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current


def fibonacci_number_again(n, m):
    assert 0 <= n <= 10 ** 18 and 2 <= m <= 10 ** 3
    a = 0
    b = 1
    pisano_period = 0
    while True:
        a, b = b, (a+b)%m
        pisano_period +=1
        if a == 0 and b == 1:
            n = n%pisano_period
            a, b = 0, 1
            if n < 2:
                return n
            for i in range(n-1):
                a, b = b, (a + b)%m
            return b




if __name__ == '__main__':
    input_n, input_m = map(int, input().split())
    print(fibonacci_number_again(input_n, input_m))
