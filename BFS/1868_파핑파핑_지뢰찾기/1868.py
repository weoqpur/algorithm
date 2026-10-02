import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(input()) for _ in range(N)]
    res = 0
    visited = [[False] * N for _ in range(N)]  # 방문 여부를 확인할 수 있는 변수
    dxy = [[1, 1], [1, 0], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]


    # 맵을 쫙 돌면서, 폭탄의 개수를 세준다.
    # 1. 각 빈 칸 . 마다 주변 8칸에 지뢰 * 가 몇 개인지 센다.
    # 2. 주변 지뢰 수가 0인 칸을 찾는다.
    # 3. 아직 열지 않은 0칸을 발견하면 클릭 횟수를 1 증가시킨다.
    # 4. 그 칸에서 BFS/DFS를 시작한다.
    #   1. 현재 칸을 연다.
    #   2. 현재 칸이 0이면 주변 8칸도 연다.
    #   3. 주변 칸 중 0이 또 있으면 계속 퍼진다.
    #   4. 숫자가 있는 칸은 열리기는 하지만, 거기서 더 퍼지지는 않는다.
    # 5. 모든 0 영역을 처리한 뒤에도 아직 열리지 않은 빈 칸이 남을 수 있다.
    #   1. 이런 칸들은 주변에 지뢰가 있어서 숫자가 1 이상인 칸이다.
    #   2. 자동으로 안 열렸으므로 각각 직접 한 번씩 클릭해야 한다.
    #   3. 남은 빈 칸 수를 답에 더한다.

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '*':
                visited[i][j] = True
                continue

            boom_cnt = 0
            for dx, dy in dxy:
                ni, nj = i + dx, j + dy
                if 0 > ni or N <= ni or 0 > nj or N <= nj: continue
                if matrix[ni][nj] == '*':
                    boom_cnt += 1
            matrix[i][j] = boom_cnt

    def bfs(i, j):
        if matrix[i][j] != 0 or visited[i][j]:
            visited[i][j] = True
            return
        visited[i][j] = True
        for dx, dy in dxy:
            ni, nj = dx + i, dy + j
            if 0 > ni or N <= ni or 0 > nj or N <= nj: continue
            bfs(ni, nj)

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and matrix[i][j] == 0:
                bfs(i, j)
                res += 1

    for i in range(N):
        res += visited[i].count(False)
    print(f"#{tc} {res}")



