import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    tmp = list(map(int, input().split()))
    oven = deque([None] * N)
    turn = 0
    circle_q = deque([i+1, tmp[i]] for i in range(M))

    while True:
        oven.rotate(-1)
        check = oven.pop()
        if check is None:
            oven.append(circle_q.popleft())
            continue

        if not oven and not circle_q:
            print(f"#{test_case} {check[0]}")
            break

        check[1] = check[1] // 2
        if check[1] == 0:
            if circle_q:
                oven.append(circle_q.popleft())
        else: oven.append(check)



