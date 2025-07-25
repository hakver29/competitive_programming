import math
import itertools
from functools import cache


def path_length(a: int, b: int, c: int) -> float:
    return math.sqrt(((a * b) / (b + c)) ** 2 + b**2) + math.sqrt(
        (a - (a * b) / (b + c)) ** 2 + c**2
    )

def shortest_path_is_integer(a, b, c) -> bool:
    numerator_1 = a**2 * b**2 + b**2 * (b + c) ** 2
    sqrt_1 = int(math.sqrt(numerator_1))
    if sqrt_1**2 != numerator_1:
        return False
    numerator_2 = (a * (b + c) - a * b) ** 2 + c**2 * (b + c) ** 2
    sqrt_2 = int(math.sqrt(numerator_2))
    denominator = b + c
    return sqrt_2**2 == numerator_2 and (sqrt_1 + sqrt_2) % denominator == 0

def solution() -> int:
    result = 0
    for a in itertools.count(1):
        print(a, result)
        for b in range(1, a + 1):
            for c in range(1, b + 1):
                if shortest_path_is_integer(a, b, c):
                    result += 1
                    if result > 1_000_000:
                        return a


print(solution())