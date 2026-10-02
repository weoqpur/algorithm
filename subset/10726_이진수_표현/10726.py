import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    target = 2**N
    if (M % target) == target-1:
        print(f"#{test_case} ON")
    else:
        print(f"#{test_case} OFF")