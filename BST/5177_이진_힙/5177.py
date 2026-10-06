import sys
sys.stdin = open("input.txt")


class MinHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def sum_parent(self, idx):
        parent = idx
        sum_v = 0
        while parent != 0:
            parent = (parent - 1) // 2
            sum_v += self.heap[parent]
        return sum_v


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = list(map(int, input().split()))

    heap = MinHeap()

    for num in nodes:
        heap.heappush(num)

    print(f"#{tc} {heap.sum_parent(len(heap.heap) - 1)}")