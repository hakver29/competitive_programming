from collections import deque

# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#


def solve_bfs(n, a, b):
    visited = [[-1 for i in range(n)] for j in range(n)]
    visited[0][0] = 0

    queue = deque([(0, 0)])

    moves = [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]

    while queue:
        current_row, current_col = queue.popleft()

        if current_row == n - 1 and current_col == n - 1:
            return visited[current_row][current_col]

        for move_row, move_col in moves:
            next_row = current_row + move_row
            next_col = current_col + move_col

            if (
                0 <= next_row < n
                and 0 <= next_col < n
                and visited[next_row][next_col] == -1
            ):
                visited[next_row][next_col] = visited[current_row][current_col] + 1
                queue.append((next_row, next_col))

    return -1
    # Write your code here


def knightlOnAChessboard(n):
    results = [[0 for _ in range(n - 1)] for _ in range(n - 1)]

    for a in range(1, n):
        for b in range(1, n):
            if results[b - 1][a - 1] != 0:
                results[a - 1][b - 1] = results[b - 1][a - 1]
                continue

            min_moves = solve_bfs(n, a, b)
            results[a - 1][b - 1] = min_moves

    return results


if __name__ == "__main__":
    n = int(input().strip())

    # Call the function and get the result
    result = knightlOnAChessboard(n)

    # Print the result to the console for local testing
    for row in result:
        print(*row)
