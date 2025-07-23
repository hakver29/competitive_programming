from itertools import permutations
numbers = [1, 2, 3, 4, 5]


# Generate all permutations
all_permutations = list(permutations(numbers))
def main():
    distinct_orderings = list(permutations(numbers))

    # Print results
    for order in distinct_orderings:
        print(list(order))


main()