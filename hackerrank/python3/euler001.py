def sum_multiples(limit, factor):
    count = (limit - 1) // factor

    return factor * count * (count + 1) // 2


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())

    sum3 = sum_multiples(n, 3)
    sum5 = sum_multiples(n, 5)
    sum15 = sum_multiples(n, 15)

    result = sum3 + sum5 - sum15
    print(result)
