import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = 4
    matrix = [input().split() for _ in range(N)]

    dxy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    pw_list = []

    def dfs(x, y, string):
        if len(string) == 7:
            if not string in pw_list: pw_list.append(string)
            return

        for dx, dy in dxy:
            tmp_x = dx + x
            tmp_y = dy + y
            if (0 > tmp_x) or (tmp_x >= N) or (0 > tmp_y) or (tmp_y >= N): continue
            dfs(tmp_x, tmp_y, string+matrix[tmp_x][tmp_y])

    for i in range(N):
        for j in range(N):
            dfs(i, j, matrix[i][j])

    print(f"#{test_case} {len(pw_list)}")