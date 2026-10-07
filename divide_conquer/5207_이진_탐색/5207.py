import sys
sys.stdin = open("input.txt")


# 목표숫자를 받고 A list 길이를 측정한 뒤 l, r 포인터에 0, len() -1 할당
# l과 r 사이의 m 배정 target보다 크면 l을 m 뒤로 작으면 r을 m 뒤로
# 위를 반복 값을 찾는 다면 중단 후 result += 1 값이 없다면 그냥 종료

def binary_search(target):
    global result
    l, r = 0, len(a_list) - 1

    while l <= r:
        m = (r + l) // 2
        if a_list[m] == target:
            result += 1
            return
        elif a_list[m] > target:
            r = m - 1
        else:
            l = m + 1
    return


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))

    result = 0

    for b in b_list:
        binary_search(b)

    print(f"#{tc} {result}")