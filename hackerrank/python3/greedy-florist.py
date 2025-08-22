#!/bin/python3


# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    print(k, c)
    S = 0
    c.sort(reverse=True)
    j = 0
    for i in range(len(c)):
        print(i)
        S += (1 + j) * c[i]
        if (i + 1) % k == 0:
            j += 1

    return S


if __name__ == "__main__":
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)
