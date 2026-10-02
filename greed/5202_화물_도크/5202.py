import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    T_table = [list(map(int, input().split())) for _ in range(N)]

    T_table.sort(key=lambda x:x[1])
    result = 1
    start = T_table[0]

    for T in T_table[1:]:
        if start[1] > T[0]: continue
        result += 1
        start = T

    print(f'#{test_case} {result}')
