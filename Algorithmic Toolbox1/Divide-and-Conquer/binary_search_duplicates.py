# python3

def binary_search_duplicate(keys, query):
   # assert all(keys[i] <= keys[i + 1] for i in range(len(keys) - 1))
   # assert 1 <= len(keys) <= 3 * 10 ** 4

    low = 0
    high = len(keys)-1
    index = -1
    while low <= high:
        middle = (low + high) // 2
        if query == keys[middle]:
            index = middle
            high = middle -1
        elif query < keys[middle]:
            high = middle -1
        else:
            low = middle + 1

    return index


if __name__ == '__main__':
    input()
    input_keys = list(map(int, input().split()))
    input()
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search_duplicate(input_keys, q), end=' ')