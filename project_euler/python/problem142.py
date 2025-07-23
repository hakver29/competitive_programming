"""
x > y > z
a^2 + b^2 > e^2 + f^2
c^2 + d^2 > e^2 + f^2
a^2 + b^2 = c^2 + d^2

x+y = a^2
x-y = b^2
x+z = c^2
x-z = d^2
y+z = e^2
y-z = f^2

2x = a^2 + b^2
2x = c^2 + d^2
a^2 + b^2 = c^2 + d^2

2y = e^2 + f^2
2y = a^2 - b^2 = (a-b)(a+b)

2z = c^2 - d^2 = (c-d)(c+d)
2z = e^2 - f^2 = (e-f)(e+f)


y,z even
y = 2y1
4y1 = e^2 + f^2 -> e = 2e1, f=2f1
4x = a^2 + b^2 + c^2 + d^2

4x = 2a^2 + 2b^2
2x = a^2 + b^2

4x + 2y = a^2 + b^2 + c^2 + d^2 + e^2 + f^2
"""

def check_tuple(x,y,z, squares):
    S = 0
    S += x + y in squares
    S += x - y in squares
    S += x + z in squares
    S += x - z in squares
    S += y + z in squares
    S += y - z in squares
    """
    L = []
    if x+y in squares:
        L.append(1)
    if x-y in squares:
        L.append(2)
    if x+z in squares:
        L.append(3)
    if x-z in squares:
        L.append(4)
    if y+z in squares:
        L.append(5)
    if y-z in squares:
        L.append(6)
    
    if S >= 4:
        print(L)
    """

    return S

def get_squares(limit):
    return [i**2 for i in range(1, limit + 1)]

def main():
    L = 10000
    squares = get_squares(L)

    for x in range(5,L//2,2):
        for y in range(2,x, 2):
            for z in range(2,y,2):
                S = check_tuple(x,y,z, squares)
                if S >= 5:
                    print(S, x,y,z)
                if S == 6:
                    return

main()

