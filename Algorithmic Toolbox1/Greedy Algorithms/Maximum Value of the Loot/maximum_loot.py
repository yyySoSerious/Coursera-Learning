# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    compounds = sorted([(prices[i]/weights[i], weights[i])
                        for i in range(len(weights))],
                       key=lambda items: items[0],
                       reverse=True)
    total_price = 0
    for i in range(len(weights)):
        if not capacity:
            return total_price
        curr_weight = min(capacity, compounds[i][1])
        total_price += curr_weight * compounds[i][0]
        capacity -= curr_weight

    return total_price


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
