import sys
sys.stdin = open("input.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for _ in range(1, 11):
    tc = input()
    N = 100
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dxy = [[-1, 0], [0, 1], [0, -1]]
    # 1. 시작점의 오른쪽 왼쪽에 길이 있는지 확인
    # 2. 있다면 그 방향으로 계속 이동
    # 3. 왔던길은 0으로 변환 후 이동
    # 4. 2가 나왔다면 루프 종료 후 시작 인덱스 반환
    x = 99
    y = matrix[99].index(2)
    while x != 0:
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if matrix[x+dx][y+dy] == 0: continue
            matrix[x][y] = 0
            x, y = x+dx, y+dy
    print(f"{tc} {y}")


