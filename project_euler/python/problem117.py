from itertools import combinations, permutations
import math

def colorPermutations(size1, size2, size3, N):
    S = 0
    for i in range(N//size1+1):
        for j in range(N//size2+1):
            for k in range(N//size3+1):

                I = [size1 for _ in range(i)]
                J = [size2 for _ in range(j)]
                K = [size3 for _ in range(k)]

                A = I + J + K
                if sum(A) <= N:
                    x = len(I)
                    y = len(J)
                    z = len(K)

                    a = 0
                    while sum(A) != N:
                        A.append(1)
                        a += 1

                    print(A, a+x+y+z, x+y+z)
                    X = math.factorial(len(A)) // (math.factorial(a) * math.factorial(x) * math.factorial(y) * math.factorial(z))
                    S += X

    return S

def main():
    N = 50
    return colorPermutations(2,3,4, N)

print(main())
