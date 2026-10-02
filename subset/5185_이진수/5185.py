import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    N, hex_num = list(map(str, input().split()))
    N = int(N)
    print("#"+str(test_case), end=" ")
    for num in hex_num:
        print(format(int(num, 16), '04b'), end="")
    print("")