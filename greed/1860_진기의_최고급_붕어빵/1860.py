import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))
    customer = list(map(int, input().split()))
    customer.sort()

    fish_bread = 0
    result = 1
    for i in range(max(customer)+1):
        if i != 0 and i % M == 0: fish_bread += K
        if (i in customer) and fish_bread == 0:
            result = 0
            break
        elif i in customer:
            if customer.count(i) < 1:
                fish_bread -= customer.count(i)
            else: fish_bread -= 1
    print(f"#{test_case} {'Possible' if result == 1 else 'Impossible'}")