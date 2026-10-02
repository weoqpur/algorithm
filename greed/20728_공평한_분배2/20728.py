import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    pockets_num, P = list(map(int, input().split()))
    candy_pockets = list(map(int, input().split()))

    # 사탕주머니에 든 사탕을 내림차순 정렬
    candy_pockets = sorted(candy_pockets, reverse=True)
    # N = 분배하고 남은 사탕주머니 수
    N = pockets_num - P - 1
    minimum = candy_pockets[0] - candy_pockets[pockets_num-1]

    # 남은 횟수만큼
    for i in range(N):
        tmp = candy_pockets[i] - candy_pockets[i+(P-1)]
        minimum = min(minimum, tmp)
    print(f"#{test_case} {minimum}")
