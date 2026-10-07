import sys
sys.stdin = open("input.txt")


class MaxHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def heappop(self):
        # print(self.heap is None)
        if self.heap:
            tmp = self.heap[0]
            last = self.heap.pop()
            if not self.heap:
                return tmp
            self.heap[0] = last
            self._siftdown(0)
            return tmp
        else:
            return -1

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _siftdown(self, idx):
        size = len(self.heap)
        largest = idx
        left = idx * 2 + 1
        right = left + 1

        if left < size and self.heap[left] > self.heap[largest]: largest = left
        if right < size and self.heap[right] > self.heap[largest]: largest = right
        if largest != idx:
            self.heap[largest], self.heap[idx] = self.heap[idx], self.heap[largest]
            self._siftdown(largest)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nodes = [list(map(int, input().split())) for _ in range(N)]
    result = "#" + str(tc)
    heap = MaxHeap()

    for node in nodes:
        if node[0] == 1:
            heap.heappush(node[1])
        elif node[0] == 2:
            pop_v = heap.heappop()
            result += " " + str(pop_v)

    print(result)