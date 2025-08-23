def max_pairwise_product1(numbers):
    max_product = float('-inf')
    numbers_length = len(numbers)
    for i in range(numbers_length):
        for j in range(i+1, numbers_length):
            product = numbers[i] * numbers[j]
            if product > max_product:
                max_product = product

    return max_product

def max_pairwise_product2(numbers):
    max_index1, max_index2 = -1, -1
    max_product = float('-inf')
    numbers_length = len(numbers)
    for i in range(numbers_length):
        if max_index1 == -1 or numbers[i] > numbers[max_index1]:
            max_index1 = i
    for i in range(numbers_length):
        if (i != max_index1) and (max_index2 == -1 or numbers[i] > numbers[max_index2]):
            max_index2 = i

    return numbers[max_index1] * numbers[max_index2]

if __name__ == '__main__':
    _ = input()
    numbers = list(map(int, input().split()))
    print(max_pairwise_product2(numbers))