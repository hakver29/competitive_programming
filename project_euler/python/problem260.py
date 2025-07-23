
def isDefaultWinningPosition(a,b,c):
    if a == b and b == c and c == a:
        return True

    if (a == b and c == 0) or (b == c and a == 0) or (a == c and b == 0):
        return True

    if (a == 0 and b == 0) or (b == 0 and c == 0) or (b == 0 and c == 0):
        return True

    return False

def nextMove(a,b,c):
    M = [(0,b-a,c-a),(a-b,0,c-b),(a-c,b-c,0),(0,b-a,c),(0,b,c-a),(a-b,0,c),(a,0,c-b),(a,b-c,0),(a-c,b,0),(a,b,0),(a,0,c),(0,b,c),(a,b-a,c),(a,b,c-a),(a-b,b,c),(a,b,c-b),(a-c,b,c),(a,b-c,c)]

    N = []
    for i in M:
        if i != (a,b,c) and i[0] >= 0 and i[1] >= 0 and i[2] >= 0:
            N.append(i)

    if a == 0 and b == 1 and c == 3:
        print((a,b,c), N)
    return N

def checkAllPositions(a,b,c, A):
    if isDefaultWinningPosition(a,b,c) == True:
        return 1
    else:
        moves = nextMove(a, b, c)

        for i in moves:
            if A[(i[0], i[1], i[2])] == 0:
                return 1
            #if i[0] ^ i[1] ^ i[2] > 0:
            #    return 1
        return 0

    return None

def main():
    N = 10
    A = {(0,0,0): 0}
    for i in range(1, N+1):
        A[(i,i,i)] = 1
        A[(0, i, i)] = 1
        A[(i, 0, i)] = 1
        A[(i, i, 0)] = 1

        A[(i, 0, 0)] = 1
        A[(0, i, 0)] = 1
        A[(0, 0, i)] = 1

    S = 0

    for i in range(N+1):
        for j in range(i+1):
            for k in range(j+1):
                value = checkAllPositions(k,j,i,A)
                A[(k, i, j)] = value
                A[(k, j, i)] = value
                A[(j, k, i)] = value
                A[(i, k, j)] = value
                A[(i, j, k)] = value
                A[(j, i, k)] = value
                S += i + j + k

    for i in range(N + 1):
        for j in range(i + 1):
            for k in range(j + 1):
                if A[(i,j,k)] == 0:
                    S += i+j+k


    print(A)
    print(S)


main()