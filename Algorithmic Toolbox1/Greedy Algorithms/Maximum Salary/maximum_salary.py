# python3
import math
from itertools import permutations
import functools

def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def compare_strings(a, b):
    if a + b > b + a:
        return -1
    elif b + a > a + b:
        return 1
    else:
        return 0

def largest_number(numbers):
    #for num in numbers:
       # assert 1 <= num <= 10**3

    numbers = [str(num) for num in numbers]
    numbers = sorted(numbers, key=functools.cmp_to_key(compare_strings))

    return int("".join(numbers))

def largest_number2(numbers):
    numbers_dict=[]
    for number in numbers:
        to_str = str(number)
        factor = math.floor(4/len(to_str))
        pad = 4 % len(to_str)
        key = to_str*factor
        if pad:
            key += to_str[-pad:]
        numbers_dict.append((key, to_str))

    numbers_dict = sorted(numbers_dict, key=lambda x: x[0], reverse=True)
    #print(numbers_dict)
    largest = [item[1] for item in numbers_dict]
    return int("".join(largest))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number2(input_numbers))
