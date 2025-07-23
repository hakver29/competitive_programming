"""
2 -> {1,2,4,6,14,30,62,126,...}
p(2) = 1/2*p(1) + 1/4 * p(2) + 1/8 * p(6) + ... + (1/2^n) * p(2^n - 2)
https://stackoverflow.com/questions/31465591/st-petersburg-lottery-probability-python
"""
import math

def p(X, c):
    return math.exp(-1.08 * 2 * X / (2 ** (2*c)))


print(1- p(2,2))
print(p(5,2))
print(p(10000, 6))
print(p(100, 10))