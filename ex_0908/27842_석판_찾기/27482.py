import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def delta(n, x, y, mat, code, t_list):
    if n == 1:
        if not code + mat[x][y] in t_list:
            t_list.append(code + mat[x][y])
    else:
        for dx, dy in dxy:
            dx += x
            dy += y
            if dx < 0 or dx >= 4 or dy < 0 or dy >= 4: continue
            delta(n-1, dx, dy, mat, code + mat[x][y], t_list)


for test_case in range(1, T + 1):
    N = 4
    matrix = [list(map(str, input().split())) for _ in range(N)]
    result_list = []
    for i in range(N):
        for j in range(N):
            x, y = i, j
            delta(7, x, y, matrix, "", result_list)

    print(f"#{test_case} {len(result_list)}")
