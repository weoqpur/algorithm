import sys
import heapq, math

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]

    graph = {}
    for edge in edges:
        if graph.get(edge[0]): graph[edge[0]][edge[1]] = edge[2]
        else: graph[edge[0]] = {edge[1]: edge[2]}

    distances = {v: math.inf for v in graph}
    distances[0] = 0
    min_heap = []
    heapq.heappush(min_heap, [0, 0])


    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if distances[current_vertex] < current_distance: continue

        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distances.get(adjacent) is None: continue
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])

    print(f"#{tc} {distances[N-1] if distances[N-1] != math.inf else 'impossible'}")