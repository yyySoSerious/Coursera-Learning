# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    coordinates = []
    for coord in starts:
        coordinates.append((coord, 0, -1))
    for i, coord in enumerate(points):
        coordinates.append((coord, 1, i))
    for coord in ends:
        coordinates.append((coord, 2, -1))
    coordinates.sort()

    count = [0] * len(points)
    num_open_segments = 0
    for _, coord_type, index in coordinates:
        if coord_type == 0:
            num_open_segments += 1
        elif coord_type == 2:
            num_open_segments -= 1
        else:
            count[index] = num_open_segments

    return count


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
