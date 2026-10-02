import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    container = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    weights.sort(reverse=True)
    container.sort(reverse=True)

    if M > N:
        weights = weights[:N]

    result = 0

    for w in weights:
        for c in container:
            if w >= c:
                result += c
                container.pop(container.index(c))
                break
    print(f"#{test_case} {result}")



    # weights.sort(key=lambda x:x[1])