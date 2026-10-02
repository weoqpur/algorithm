import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = 9
    result = 1
    matrix = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        row = 0
        col = 0

        for j in range(N):
            row += matrix[i][j]
            col += matrix[j][i]
            if j % 3 == 0 and i % 3 == 0:
                tmp_list = list()
                for k in range(3):
                    for a in range(3):
                        tmp_list.append(matrix[i+k][j+a])
                for tmp in tmp_list:
                    if tmp_list.count(tmp) > 1:
                        result = 0
        if row != 45 or col != 45:
            result = 0
    print(f"#{test_case} {result}")
    # ///////////////////////////////////////////////////////////////////////////////////
