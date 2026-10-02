import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    height_list = list(map(int, input().split()))

    result = float('inf')


    def comb_sum(n, height):
        global result
        if B <= height:
            result = min(result, height-B)
            return
        if n == N: return
        comb_sum(n+1, height)
        comb_sum(n+1, height+height_list[n])

    comb_sum(0, 0)

    print(f"#{test_case} {result}")

