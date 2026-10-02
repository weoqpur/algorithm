import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    row = 1
    col = 1
    for i in range(N-M):
        for j in range(N-M):
            if i+M+1 < N:
                if matrix[i:i+M][j].count(1) == M and matrix[i+M+1][j] == 0:
                    pass
            if j != 0 and i == 0:
                matrix[j]
    # ///////////////////////////////////////////////////////////////////////////////////