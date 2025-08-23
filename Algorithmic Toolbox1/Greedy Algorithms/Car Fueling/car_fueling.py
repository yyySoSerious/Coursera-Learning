# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    n = len(stops)
    stops += [d]
    refill_stop = 0
    num_refills = 0
    i = 0
    while i < n:
        if stops[i + 1] - stops[i] > m:
            return -1
        curr_distance = stops[i + 1] - refill_stop
        if curr_distance > m:
            num_refills += 1
            refill_stop = stops[i]
        i += 1

    return num_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
