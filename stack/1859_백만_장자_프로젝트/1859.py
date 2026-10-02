import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    vactor = list(map(int, input().split()))
    result = 0
    sell_p = vactor[-1]
    for vac in vactor[::-1]:
        if sell_p < vac:
            sell_p = vac
            continue
        result += sell_p - vac
    print(f"#{test_case} {result}")