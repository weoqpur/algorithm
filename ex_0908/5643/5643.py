import sys
import pprint
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 사람의 수
    M = int(input()) # 비교의 수
    rel = [list(map(str, input().split())) for _ in range(M)]

    result = 0 # 순서를 알 수 있는 사람의 수

    # 번호 별로 사람 수만큼의 길이의 리스트를 벨류로 가진 딕셔너리
    heights = {str(i): [0 for _ in range(N)] for i in range(1, N + 1)}
    heights_list = [[False] * N for _ in range(N)]

    for short, long in rel:
        heights[long][int(short)-1] -= 1
        heights[short][int(long)-1] += 1

    def trac(start, num, direction):
        for i, arr in enumerate(heights[num]):
            if arr * direction > 0 and not visited[i]:
                visited[i] = True
                heights_list[start][i] = True
                trac(start, str(i+1), direction)

    for key in heights.keys():
        start = int(key) - 1
        for direction in (1, -1):
            visited = [False] * N
            visited[start] = True
            trac(start, key, direction)

    for visit in heights_list:
        if visit.count(False) == 1: result += 1

    print(f"#{test_case} {result}")

