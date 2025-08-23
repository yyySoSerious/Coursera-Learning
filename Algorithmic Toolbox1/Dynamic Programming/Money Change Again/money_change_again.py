# python3


def change_naive(money):
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    minimum = [float("inf")] * (money+1)
    minimum[0] = 0
    for amount in range(1, money+1):
        for coin in [1, 3, 4]:
            leftover_amount = amount-coin
            if leftover_amount >= 0:
                minimum[amount] = min(minimum[amount], 1+minimum[leftover_amount])

    return minimum[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
