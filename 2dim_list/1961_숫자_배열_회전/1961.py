import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print(f"#{test_case}")
    for i in range(N):
        start, middle, end = "", "", ""
        for j in range(N):
            start += str(matrix[N-1-j][i])
            middle += str(matrix[N-1-i][N-1-j])
            end += str(matrix[j][N-1-i])
        print(start, middle, end)



