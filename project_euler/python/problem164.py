from functools import cache


@cache
def getNextValueOptions(current):
    if current == "":
        return [str(i) for i in range(1,10)]
    elif len(current) == 1:
        return [str(i) for i in range(0,10 - int(current))]
    else:
        return [str(i) for i in range(0, 10 - int(current[-1]) - int(current[-2]))]

def aggregate_keys(dictionary, n):
    if n < 3:
        return dictionary
    aggregated_dict = {}
    for key in dictionary:
        last_three_chars = key[0][-3:]
        if (last_three_chars, n) not in aggregated_dict:
            aggregated_dict[(last_three_chars, n)] = dictionary[key]
        else:
            aggregated_dict[(last_three_chars, n)] += dictionary[key]
    return aggregated_dict

def main():
    n = 0
    N = {}
    N_prev = {}

    S = getNextValueOptions("")

    while n < 20:
        if n == 0:
            for i in S:
                if not (i,n) in N:
                    N[(i, n)] = 1
                else:
                    N[(i, n)] += 1
        elif n <= 2:
            for key in list(N):
                K = key[0]
                S = getNextValueOptions(K)
                for i in S:
                    N[(K + i, n)] = 1
        else:
            N_prev = aggregate_keys(N_prev, n)
            for key in list(N_prev):
                K = key[0]
                S = getNextValueOptions(K)
                for i in S:
                    if (K,n) in N_prev and (K[-2:] + i, n) not in N:
                        N[(K[-2:] + i, n)] = N_prev[(K,n)]
                    elif (K,n) in N_prev and (K[-2:] + i, n) in N:
                        N[(K[-2:] + i, n)] += N_prev[(K, n)]
                    elif (K, n) not in N_prev and (K[-2:] + i, n) not in N:
                        N[(K[-2:] + i, n)] = 1
                    elif (K, n) not in N_prev and (K[-2:] + i, n) in N:
                        N[(K[-2:] + i, n)] += 1

        N = {key: value for key, value in N.items() if key[1] == n}
        N_prev = N
        n += 1

    return sum(N.values())

print(main())