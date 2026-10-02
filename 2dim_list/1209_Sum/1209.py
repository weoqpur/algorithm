import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case_num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0
    cross_value = 0
    r_cross_value = 0
    result = 0
    for i in range(100):
        temp_max_value_n = 0
        temp_max_value_m = 0
        for j in range(100):
            temp_max_value_n += matrix[i][j]
            temp_max_value_m += matrix[j][i]
            if i == j: cross_value += matrix[i][j]
            if 99 - i == j: r_cross_value += matrix[i][j]
        max_value = max(temp_max_value_n, temp_max_value_m, max_value)
    result = max(max_value, r_cross_value, cross_value)
    print(f'#{test_case} {result}')


    # ///////////////////////////////////////////////////////////////////////////////////
