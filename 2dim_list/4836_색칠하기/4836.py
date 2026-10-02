import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    zero_map = [[0] * 10 for _ in range(10)]
    result = 0
    for v in matrix:
        for i in range(10):
            for j in range(10):
                if v[0] <= i <= v[2] and v[1] <= j <= v[3] \
                        and zero_map[i][j] != v[4] and zero_map[i][j] != 3:
                    zero_map[i][j] += v[4]

    for aws in zero_map:
        result += aws.count(3)
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
