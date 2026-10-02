import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    tmp_min = float("inf")
    for i in range(N):
        for j in range(N):
            tmp_max = 0
            for k in range(N):
                tmp_max += matrix[i][k]
                tmp_max += matrix[k][j]
            tmp_max -= matrix[i][j]
            tmp_min = min(tmp_max, tmp_min)
            result = max(result, tmp_max)

    print(f"#{test_case} {result-tmp_min}")
