import sys
sys.stdin = open("input.txt")


class Heap:
    def __init__(self):
        self.heap = []

    def heap_min_push(self, item):
        self.heap.append(item)
        self._min_heap_siftup(len(self.heap) - 1)

    def _min_heap_siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[parent] > self.heap[idx]:
            self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
            idx = parent
            parent = (idx - 1) // 2

    def _min_heap_siftdown(self, idx):
        size = len(self.heap)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < size and self.heap[left] < self.heap[largest]: largest = left
        if right < size and self.heap[right] < self.heap[largest]: largest = right
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._min_heap_siftdown(largest)

    def heap_min_pop(self):
        tmp = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self._min_heap_siftdown(0)
        return tmp


T = int(input())
for tc in range(1, T + 1):
    N, fs_num = map(int, input().split())
    num_list = [list(map(int, input().strip().split())) for _ in range(N)]
    result = 0

    max_heap = Heap()
    min_heap = Heap()

    max_heap.heap_min_push(-fs_num)

    for fs, ls in num_list:
        if -max_heap.heap[0] > fs: max_heap.heap_min_push(-fs)
        else: min_heap.heap_min_push(fs)
        if -max_heap.heap[0] > ls: max_heap.heap_min_push(-ls)
        else: min_heap.heap_min_push(ls)

        if len(max_heap.heap) <= len(min_heap.heap):
            max_heap.heap_min_push(-min_heap.heap_min_pop())
        elif len(max_heap.heap) > (len(min_heap.heap) + 1):
            min_heap.heap_min_push(-max_heap.heap_min_pop())
        result = (result + (-max_heap.heap[0])) % 20171109

    print(f"#{tc} {result}")