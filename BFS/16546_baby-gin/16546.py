import sys
sys.stdin = open("input.txt", "r")
import itertools

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = list(map(int, input().strip().expandtabs()))
    is_babygin = False
    number = itertools.permutations(number)

    for perm in number:
        start = perm[:3]
        end = perm[3:]

        if ((start[0] + 2 == start[1] + 1 == start[2]) or (start[0] == start[1] == start[2])) \
                and ((end[0] + 2 == end[1] + 1 == end[2]) or (end[0] == end[1] == end[2])):
            is_babygin = True
            break
    if is_babygin:
        print(f"#{test_case} true")
    else:
        print(f"#{test_case} false")

