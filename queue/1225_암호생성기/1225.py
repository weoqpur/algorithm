import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    t = int(input())
    pw = list(map(int, input().split()))
    capa = len(pw)
    idx = 0
    cnt = 1

    while pw[idx] != 0:
        pw[idx] -= cnt
        if pw[idx] <= 0:
            pw[idx] = 0
            break
        idx += 1
        cnt = cnt % 5 + 1
        idx = idx % capa
    print(f"#{test_case}", end=" ")
    for i in range(capa):
        print(pw[(i+idx+1) % 8], end=" ")
    print(" ")
