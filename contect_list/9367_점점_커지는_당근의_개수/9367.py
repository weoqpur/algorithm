import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))

    result = 1
    cnt = 1
    for i in range(N-1):
        if num_list[i] < num_list[i+1]: cnt += 1
        else: cnt = 1
        result = max(result, cnt)
    print(f"#{test_case} {result}")
