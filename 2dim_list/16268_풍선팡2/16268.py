import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    result = 0

    for i in range(N):
        for j in range(M):
            sum_value = matrix[i][j]
            for x_t, y_t in zip(dx, dy):
                x, y = i+x_t, j+y_t
                if 0 <= x < N and 0 <= y < M:
                    sum_value += matrix[x][y]
            result = max(result, sum_value)

    print(f'#{test_case} {result}')