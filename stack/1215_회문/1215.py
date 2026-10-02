import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    N = int(input())
    M = 8
    matrix =[input() for _ in range(M)]
    result = 0

    for i in range(M):
        for j in range(M-N+1):
            row = ""
            col = ""
            for k in range(N):
                row += matrix[j+k][i]
                col += matrix[i][j+k]
            if row == row[::-1]: result += 1
            if col == col[::-1]: result += 1
    print(f"#{test_case} {result}")



