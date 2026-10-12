import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, target = map(int, input().split())

    n_list = [0] * (target+1)
    n_list[0] += 1

    for i in range(1, N+1):
        for dp in range(target, i - 1, -1):
            n_list[dp] += n_list[dp - i]

    print(f"#{tc} {n_list[target]}")
