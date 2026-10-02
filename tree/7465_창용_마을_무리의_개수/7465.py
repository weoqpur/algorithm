import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    node_input_list = [list(map(int, input().split())) for _ in range(M)]

    rank = [0] * (N+1)
    p = list(range(N+1))

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])
        return p[x]

    def union(x, y):
        px = find_set(x)
        py = find_set(y)

        if px != py:
            if rank[py] > rank[px]:
                p[px] = py
            elif rank[px] > rank[py]:
                p[py] = px
            else:
                p[py] = px
                rank[px] += 1

    for node in node_input_list:
        union(node[0], node[1])

    for i in range(1, N+1):
        p[i] = find_set(i)

    print(f"#{tc} {len(set(p)) - 1}")