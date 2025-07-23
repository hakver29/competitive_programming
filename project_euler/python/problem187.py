import math
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


def main():
    S = 0
    N = 10**8
    primes = SieveOfEratosthenes(N)
    print("test")

    for i in range(2,N):
        if i % 10000 == 0:
            print(i)
        if i not in primes:
            max = math.floor(math.sqrt(i))
            for j in range(2,max+1):
                if i % j == 0:
                    r = i / j
                    if r in primes and j in primes:
                        # print(r,j)
                        S += 1

    print(S)


main()