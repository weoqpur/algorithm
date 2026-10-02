import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    num_list = [i for i in range(1, 13)]

    def sum_subset(depth, subset_list):
        global result

        if len(subset_list) == N and sum(subset_list) == M:
            result += 1
            return
        if len(subset_list) > N or sum(subset_list) > M: return
        if depth == len(num_list): return

        sum_subset(depth+1, subset_list)
        subset_list2 = subset_list[:]
        subset_list2.append(num_list[depth])
        sum_subset(depth+1, subset_list2)

    result = 0
    sum_subset(0, list())
    print(f"#{test_case} {result}")