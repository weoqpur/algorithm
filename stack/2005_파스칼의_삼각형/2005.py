import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    last = []
    print(f"#{test_case}")
    for i in range(1, N+1):
        tmp = [1]
        print("1", end=" ")
        for j in range(1, i):
            if i != 2:
                if j == i-1: break
                tmp.append(last[-1][j-1] + last[-1][j])
                print(last[-1][j-1] + last[-1][j], end=" ")
        if i != 1:
            tmp.append(1)
            print("1", end=" ")
        print("")
        last.append(tmp)
        # 1을 먼저 append 후 1앞 숫자와 함한 뒤 그 다음 숫자가 같은 숫자면 더하고 append한 뒤 작다면 그만 루프를 돈다
