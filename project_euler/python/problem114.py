"""
n = 3: 1 + 1 = 2
n = 4: 1 + 1 + 2 = 4
n = 5: 1 + 1 + 2 + 3 = 7
n = 6: 1 + 1 + 2 + 3 + 4 = 11
n = 7: 1 + 1 + 2 + 3 + 4 + 5 + 1 = 17
n = 8: 1 + 6 + 5 + 4 + 3 + 2 + 1 ´+ 1 + 2 = 27
n = 9: 1 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 1 + 2 + 3 + 4 + 1

X X X X X X X X

n > m - 1 + a1 + ... + am, m in (0, (n-1)//3), ai in (3,n) for i in (1,m)
n - m > a1 + ... + am

Finn alle permutasjoner (a1,...,am) for n in range (1,...,50)


X X X X X X

"""
from math import comb, factorial
from collections import Counter
from itertools import combinations_with_replacement, permutations

def find_combinations(n):
    min_value = 3
    max_value = n
    results = []

    for m in range(0, (n//3) + 1):
        combinations = combinations_with_replacement(range(min_value, max_value + 1 - min_value * (m-1)), m)
        results.extend(filter(lambda combo: n >= (len(combo) - 1 + sum(combo)), combinations))

    return results

def count_permutations(lst):
    """
    Returns the number of unique permutations of a list with duplicate entries.
    """
    freq = Counter(lst)  # Count occurrences of each unique number
    numerator = factorial(len(lst))  # Compute n!
    denominator = 1

    # Compute product of factorials of frequencies
    for count in freq.values():
        denominator *= factorial(count)

    return numerator // denominator


def main():
    n = 7  # Input value of n
    S = 0
    result = find_combinations(n)

    for combo in result:
        number_of_permutations = count_permutations(combo)
        possible_combinations = comb(n - sum(combo) + 1, len(combo))* number_of_permutations
        S += possible_combinations
    print(S)

main()
