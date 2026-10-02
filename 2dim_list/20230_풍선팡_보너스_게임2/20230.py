import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N):
            tmp_sum = 0
            for k in range(N):
                tmp_sum += matrix[i][k]
                tmp_sum += matrix[k][j]
            tmp_sum -= matrix[i][j]
            result = max(tmp_sum, result)
    print(f"#{test_case} {result}")