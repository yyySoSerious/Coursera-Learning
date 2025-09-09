# python3

def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n//2 - 1, -1, -1):
        min_idx = -1
        j = i
        while min_idx !=  j:
            if min_idx == -1:
                min_idx = j
            else:
                j = min_idx

            left_child_idx = (2* j) + 1
            right_child_idx = left_child_idx + 1
            if left_child_idx < n and data[left_child_idx] < data[min_idx]:
                min_idx = left_child_idx
            if right_child_idx < n and data[right_child_idx] < data[min_idx]:
                min_idx = right_child_idx
            if min_idx != j:
                swaps.append((j, min_idx))
                data[j], data[min_idx] = data[min_idx], data[j]

    return swaps

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
