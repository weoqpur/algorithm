import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edge_ls = [list(map(int, input().split())) for _ in range(E)]
    p = list(range(V+1))
    mst = 0

    # 1. kruskal 사용 우선 input 값을 2번 인덱스 기준으로 정렬
    # 2. 가중치 기준으로 정렬 되었으면 간선을 하나씩 선택
    # 3. 만약 그 간선을 선택할 시 싸이클이 발생한다면 다음으로 넘어감
    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px < py: p[py] = px
        else: p[px] = py

    edge_ls.sort(key=lambda x: x[2])
    for edge in edge_ls:
        s, e, w = edge
        if find_set(s) != find_set(e):
            union(s, e)
            mst += w

    print(f"#{tc} {mst}")