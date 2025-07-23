from itertools import combinations_with_replacement, permutations

LIMIT = 20 * 9**2
N = 2

def digit_combinations(length):
    """
    Generate all combinations of digits 1-9 with a fixed length,
    allowing repeated digits and ignoring order (e.g., '123' same as '321').
    """
    digits = '123456789'
    return [list(c) for c in combinations_with_replacement(digits, length)]

def get_squares():
    return [i*i for i in range(1, int(LIMIT ** 0.5) + 1)]

def square_digits(a):
    x = 0
    for i in a:
        x += int(i)**2
    return x

def padded_digit_permutations(digits, n):
    """
    Generate all permutations of the given digits padded with zeros to length n.
    Digits can repeat; zeros can be inserted in any position.
    """
    if len(digits) > n:
        raise ValueError("Number of digits exceeds target length.")

    num_zeros = n - len(digits)
    base_digits = list(digits) + ['0'] * num_zeros

    # Use set to remove duplicates if digits have repeated elements
    perms = set(permutations(base_digits, n))

    # Join tuples into strings or integers as needed
    return [''.join(p) for p in perms]

def get_permutations(n):
    S = 0
    squares = get_squares()
    print(n, squares)
    for i in range(1, n):
        print(i)
        combinations = digit_combinations(i)
        print(combinations)
        for combination in combinations:
            sqr_dgts = square_digits(combination)
            if sqr_dgts in squares:
                print('comb', sqr_dgts, combination, n)
                permutations = padded_digit_permutations(combination, n)
                print(permutations)

                for i in permutations:
                    print(i)
                    if i == int(i):
                        S += int(i)
    return S


def main():
    a = get_permutations(2)
    print(a)

main()

#print(len(digit_combinations(20)))