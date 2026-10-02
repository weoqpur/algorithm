import sys
sys.stdin = open("input.txt")
from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    result = 0
    for i in range(1, N+1):
        for num in combinations(num_list, i):
            if sum(num) == K:
                result += 1
    print(f"#{tc} {result}")