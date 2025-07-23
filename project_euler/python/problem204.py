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

def isHammingPrime(n, hammingPrimes):
    for i in hammingPrimes:
        if n % i == 0:
            while n % i == 0:
                n = n // i
                #print(n)
    if n == 1:
        return True
    return False
def main():
    hammingPrimes = SieveOfEratosthenes(100)
    N = 10**9
    S = 0
    for i in range(1, N+1):
        #print(i)
        S += isHammingPrime(i, hammingPrimes);
        if i % 100000000 == 0:
            print(i)
    return S
print(main())