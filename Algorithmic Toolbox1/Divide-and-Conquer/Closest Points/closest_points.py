# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_helper(sorted_points_x, sorted_points_y, n):
    if n <= 3:
        min_dist = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                min_dist = min(min_dist, distance_squared(
                    sorted_points_x[i],sorted_points_x[j]))
        return min_dist

    middle_x = n //2

    #split by boundary
    left_sorted_x = sorted_points_x[:middle_x]
    right_sorted_x = sorted_points_x[middle_x:]
    boundary_x = sorted_points_x[middle_x].x

    left_sorted_y = []
    right_sorted_y = []

    for p in sorted_points_y:
        if p.x < boundary_x:
            left_sorted_y.append(p)
        else:
            right_sorted_y.append(p)

    #find minimum from both halves
    left_d_squared = minimum_distance_helper(left_sorted_x, left_sorted_y, len(left_sorted_x))
    right_d_squared = minimum_distance_helper(right_sorted_x, right_sorted_y, len(right_sorted_x))
    d_squared = min(left_d_squared, right_d_squared)
    d_squared_sqrt = sqrt(d_squared)

    #find minimum at boundary area between the two halves
    boundary_sorted_points_y = [p for p in sorted_points_y if abs(p.x-boundary_x) < d_squared_sqrt]
    boundary_d_squared = float("inf")
    for i in range(len(boundary_sorted_points_y)):
        for j in range(i+1, len(boundary_sorted_points_y)):
            p1 = boundary_sorted_points_y[i]
            p2 = boundary_sorted_points_y[j]
            if p2.y - p1.y >= d_squared_sqrt:
                break
            boundary_d_squared = min(boundary_d_squared, distance_squared(p1, p2))

    #return global minimum
    return min(d_squared, boundary_d_squared)

def minimum_distance_squared(points):
    sorted_points_x = sorted(points, key=lambda p: p.x)
    sorted_points_y = sorted(points, key=lambda p: p.y)

    return minimum_distance_helper(sorted_points_x, sorted_points_y, len(points))


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
