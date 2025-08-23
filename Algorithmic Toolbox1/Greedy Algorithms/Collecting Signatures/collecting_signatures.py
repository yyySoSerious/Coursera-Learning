# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments = sorted(segments, key=lambda x: x[1])
    num_points = []
    n = len(segments)
    i = 0
    while i < n:
        curr_end = segments[i].end
        while i < n and segments[i].start <= curr_end:
            i += 1
        num_points.append(curr_end)

    return num_points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
