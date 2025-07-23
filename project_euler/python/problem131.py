import math
from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def SieveOfEratosthenes(num):
    P = []
    prime = [True for i in range(num + 1)]
    # boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num + 1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num + 1):
        if prime[p]:
            P.append(p)
    return P

def is_cube(n):
    cube_root = n**(1./3.)
    if round(cube_root) ** 3 == n:
        return True
    else:
        return False

def get_cube(n):
    return round(n**(1./3.))

def main():
    M = 1000000
    S = 0
    P = SieveOfEratosthenes(M)

    a = 2
    while a**3 - (a-1)**3 <= M:
        if a**3 - (a-1)**3 in P:
            S += 1
        a += 1

    return S

print(main())