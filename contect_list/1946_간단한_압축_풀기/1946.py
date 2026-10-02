import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    char_num_list = [input().split() for _ in range(N)]
    cnt = 0
    print(f"#{test_case}")
    for char, num in char_num_list:
        for i in range(int(num)):
            cnt += 1
            print(char, end="")
            if cnt%10 == 0: print(" ")
    print(" ")