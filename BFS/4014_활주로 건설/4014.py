import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, X = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    r_matrix = list(map(list, zip(*matrix[::-1])))

    result = 0
    for i in range(N):
        set_row, set_col = [False] * N, [False] * N
        row, col = True, True
        for j in range(N-1):
            if matrix[i][j+1] == matrix[i][j]+1 and row:
                if j-X+1 < 0:
                    row = False
                else:
                    tmp = matrix[i][j-X+1:j+1]
                    if tmp.count(tmp[0]) != X:
                        row = False

                    for k in range(j-X+1, j+1):
                        if not set_row[k]: set_row[k] = True
                        else:
                            row = False
            elif matrix[i][j] == matrix[i][j+1]+1 and row:
                if j+X >= N:
                    row = False
                else:
                    tmp = matrix[i][j+1:j+X+1]
                    if tmp.count(tmp[0]) != X:
                        row = False
                    for k in range(j+1, j+X+1):
                        # print(tmp, matrix[i][j], i, j)
                        if not set_row[k]: set_row[k] = True
                        else:
                            row = False
            elif (matrix[i][j]+1 < matrix[i][j+1] or matrix[i][j]-1 > matrix[i][j+1]) and row:
                row = False

            if r_matrix[i][j + 1] == r_matrix[i][j] + 1 and col:
                if j - X + 1 < 0:
                    col = False
                else:
                    tmp = r_matrix[i][j - X + 1:j + 1]
                    if tmp.count(tmp[0]) != X:
                        col = False

                    for k in range(j - X + 1, j + 1):
                        if not set_col[k]:
                            set_col[k] = True
                        else:
                            col = False
            elif r_matrix[i][j] == r_matrix[i][j + 1] + 1 and col:
                if  j + X >= N:
                    col = False
                else:
                    tmp = r_matrix[i][j + 1:j + X + 1]
                    if tmp.count(tmp[0]) != X:
                        col = False
                    for k in range(j + 1, j + X + 1):
                        # print(tmp, matrix[i][j], i, j)
                        if not set_col[k]:
                            set_col[k] = True
                        else:
                            col = False
            elif (r_matrix[i][j] + 1 < r_matrix[i][j + 1] or r_matrix[i][j] - 1 > r_matrix[i][j + 1]) and col:
                col = False
        if row: result += 1
        if col: result += 1
    print(f"#{test_case} {result}")




