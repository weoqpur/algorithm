import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [input() for _ in range(N)]
    result = ""
    for i in range(N):
        for j in range(N-M+1):
            row, col = "", ""
            for k in range(M):
                row += matrix[i][j+k]
                col += matrix[j+k][i]
            if row == row[::-1]: result = row
            if col == col[::-1]: result = col
    print(f"#{test_case} {result}")