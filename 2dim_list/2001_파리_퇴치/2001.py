import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for vac in matrix[i:i+M]:
                temp += sum(vac[j:j+M])
            max_value = max(temp, max_value)

    print(f'#{test_case} {max_value}')
    # ///////////////////////////////////////////////////////////////////////////////////
