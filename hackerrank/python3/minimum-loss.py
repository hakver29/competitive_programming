#!/bin/python3


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


def minimumLoss(price):
    min_loss = float("inf")
    map = {}
    for i in range(len(price)):
        map[price[i]] = i
    price.sort(reverse=True)
    for i in range(1, len(price)):
        if map[price[i - 1]] < map[price[i]] and price[i - 1] - price[i] < min_loss:
            min_loss = price[i - 1] - price[i]
    return min_loss


if __name__ == "__main__":
    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)
    print(result)
