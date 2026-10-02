import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    N_list = list()
    for _ in range(N):
        N_list.append(list(map(int, input().split())))
    P = int(input())
    C = list()
    for _ in range(P):
        C.append(int(input()))
    result = [0] * P
    for i, num in enumerate(C):
        for start, end in N_list:
            if start <= num <= end:
                result[i] += 1
    print("#" + str(test_case) + " " + " ".join(map(str, result)))
    # ///////////////////////////////////////////////////////////////////////////////////