def sum_two_inputs(a, b):
    return a + b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_two_inputs(a, b))