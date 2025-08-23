# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    a = 0
    b = 1
    from_index = from_index % 60
    to_index = to_index % 60
    total_sum = 0
    for i in range(to_index + 1):
        if i >= from_index:
            total_sum += a %10

        a, b = b, (a + b)

    return total_sum % 10

#calculate f_n+2 -1
def last_digit_of_the_sum_of_fibonacci_numbers(n):
    a, b = 0, 1
    n = (n+2) % 60
    if n < 2:
        return (n-1) % 10
    for _ in range(n-1):
        a, b = b, (a+b)%10
    return (b-1) % 10

def last_digit_of_the_sum_of_fibonacci_numbers_again2(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    sum_from_index = last_digit_of_the_sum_of_fibonacci_numbers(from_index-1)
    sum_to_index = last_digit_of_the_sum_of_fibonacci_numbers(to_index)
    return (sum_to_index - sum_from_index) % 10


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again2(input_from, input_to))
