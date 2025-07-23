#1:1
#1: 1*1

# 16: n, n*n, n^2 * n^2, n^4 * n^4 = n^8, n^8 * n^8 = n^16
from itertools import permutations

def m(n):
    binary_representation = bin(n)
    binary_list_str = list(str(binary_representation[2:]))
    binary_list_int = [int(i) for i in binary_list_str]

    #print(binary_list_int)
    #if len(binary_list_int) == sum(binary_list_int):
    #if sum(binary_list_int) == len(binary_list_int):
    #   return len(binary_list_int)
    if sum(binary_list_int) == 1:
        return len(binary_list_int) - 1

    print(n, binary_list_int)

# n^5 = n^2 * n^3 = n^2 * n^2 * n = 1 + 1 + 1

def getNext(L):
    next = len(L)+1
    binary_representation = bin(next)
    binary_list_str = list(str(binary_representation[2:]))
    binary_list_int = [int(i) for i in binary_list_str]
    if sum(binary_list_int) == 1:
        return len(binary_list_int) - 1

    perms = find_two_number_permutations(next)
    M = float('inf')
    print(next, L)
    for comb in perms:
        #M_temp = L[comb[0]-1]+L[comb[1]-1]
        M_temp = max(L[comb[0]-1], L[comb[1]-1])+1
        if M_temp < M:
            M = M_temp
    return M

def find_two_number_permutations(target):
    """
    Finds all unique permutations of two numbers that sum to the given target.
    """
    pairs = [(a, target - a) for a in range(1, target)]  # Generate valid pairs
    all_permutations = set()  # Use a set to store unique permutations

    for pair in pairs:
        for perm in permutations(pair):
            all_permutations.add(perm)  # Ensure unique orderings

    return sorted(all_permutations)  # Sort for readabilit

def main():
    #S = 0
    #for i in range(1, 201):
    # n*n = n^2, n^2 * n^2 = n^4, n^5 = n^4 * n, n^10 = n^5 * n^5, n^11 = n^10 * n
    #    S += m(i)
    #11 = 3 + 8 = [1,2,3], [1,2,4,8]
    # 16 = 8 + 8 = [1,2,4,8], [1,2,4,8]
    # 22 = 11 + 11 = [1,2,3,4,8]
    # 7: [1,2,3,6,7], [1,2,3,4,7]
    # 28:
    L = [[1], [1,2], [1,2,3]]
    #L = [0, 1, 2, 2, 3, 3, 4, 3, 4, 4]
    print(getNext(L))
    #print(find_two_number_permutations(10))
    #print(find_two_number_permutations(11))



    #print(M)
    #print(perm)


    print(L)

main()