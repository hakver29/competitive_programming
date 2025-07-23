from math import factorial, comb
from collections import Counter
from itertools import combinations_with_replacement, permutations

def find_combinations(n, m):
    min_value = m
    max_value = n
    results = []

    for i in range(0, (n//m) + 1):
        combinations = combinations_with_replacement(range(min_value, max_value + 1 - min_value * (i-1)), i)
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

def fill(m,n):
    S = 0
    result = find_combinations(n, m)
    for combo in result:
        number_of_permutations = count_permutations(combo)
        possible_combinations = comb(n - sum(combo) + 1, len(combo)) * number_of_permutations
        S += possible_combinations
    return S

def main():
    m = 50
    n = 1

    while fill(m,n) <= 1000000:
        n += 1

    return n

print(main())