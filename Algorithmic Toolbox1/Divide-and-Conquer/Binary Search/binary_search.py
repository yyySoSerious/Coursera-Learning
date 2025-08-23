# python3


def linear_search(keys, query):
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search_helper(keys, query, l, r):
    if l >= r:
        return -1
    middle = (l + r) //2
    if query == keys[middle]:
        return middle
    elif query < keys[middle]:
        return binary_search_helper(keys, query, l, middle)
    return binary_search_helper(keys, query, middle+1, r)

def binary_search(keys, query):
    #assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    #assert 1 <= len(keys) <= 3 * 10 ** 4

    low = 0
    high = len(keys)-1

    while low <= high:
        middle = (low + high) // 2
        if query == keys[middle]:
            return middle
        elif query < keys[middle]:
            high = middle -1
        else:
            low = middle + 1

    return -1


if __name__ == '__main__':
    input()
    input_keys = list(map(int, input().split()))
    input()
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
