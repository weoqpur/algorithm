import sys
sys.stdin = open("input.txt", "r")
from collections import deque, defaultdict

for test_case in range(1, 11):
    v_cnt, e_cnt = map(int, input().split())
    edges = list(map(int, input().split()))
    graph = defaultdict(list)
    result = []

    for i in range(e_cnt):
        graph[edges[2 * i]].append(edges[2 * i + 1])

    visited = set()

    def dfs(v):
        visited.add(v)

        for adj_v in graph[v]:
            if adj_v in visited: continue
            dfs(adj_v)

        result.append(v)

    for v in range(1, v_cnt+1):
        if v in visited: continue
        dfs(v)

    print(f"#{test_case}", *reversed(result))
