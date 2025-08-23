# python3
import math

def money_change(money):
    assert 0 <= money <= 10 ** 3
    num_coins = 0
    leftover = money
    while leftover > 0:
        if leftover >= 10:
            leftover -= 10
        elif leftover >= 5:
            leftover -= 5
        else:
            leftover -= 1
        num_coins += 1
    return num_coins

def money_change2(money):
    assert 0 <= money <= 10 ** 3

    a = math.floor(money /10)
    b = math.floor((money % 10) / 5)
    c =  (money % 10) % 5

    return a + b + c
if __name__ == '__main__':
    input_money = int(input())
    print(money_change2(input_money))
