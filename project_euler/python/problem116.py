from itertools import combinations, permutations
import math

def colorPermutations(size, N):
    S = 0
    for i in range(N//size):
        L = [size for _ in range(i+1)]
        x = len(L)

        while sum(L) != N:
            L.append(1)

        X = math.comb(len(L),x)
        S += X

    return S

def main():
    N = 50
    S = 0
    for i in range(2,5):
        S += colorPermutations(i, N)

    return S

print(main())
