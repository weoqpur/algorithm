import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    idx = [0, 0]
    for i, vac in enumerate(matrix):
        tmp = max(vac)
        max_v = max(tmp, max_v)
        if tmp > max_v:
            idx = [i, vac.index(tmp)]

    x = [0, 1, 0, -1]
    y = [1, 0, -1, 0]

    exitt = False
    i = 0
    while True:
        dx, dy = idx[0] + x[i%4], idx[1] + y[i%4]
        if 0 > dx or dy > 0 or dx >= N or dy >= N:
            continue
        tmp_x, tmp_y = idx[0], idx[1]
        if matrix[dx][dy] < max_v:
            max_v = matrix[dx][dy]
            tmp_x = dx
            tmp_y = dy
        k = 0
        for j in range(4):
            if max_v < matrix[idx[0] + x[j]][idx[1] + y[j]]: k+=1
        
        if k == 4: break
        idx = [tmp_x, tmp_y]
    print(max_v)
        
        

