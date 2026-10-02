import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[0]*N for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direction = 0
    x, y = 0, 0
    for i in range(1, N*N+1):
        nx = x+dx[direction % 4]
        ny = y+dy[direction % 4]
        if 0 > nx or nx >= N or 0 > ny or ny >= N or matrix[nx][ny] != 0:
            direction += 1
        matrix[x][y] = i
        x += dx[direction % 4]
        y += dy[direction % 4]

    print("#"+str(test_case))
    for i in matrix:
        for j in i:
            print(j, end=" ")
        print("")

