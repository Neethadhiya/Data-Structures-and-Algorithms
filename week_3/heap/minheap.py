class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return 2 * index + 1

    def right_child(self, index):
        return 2 * index + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, index):
        if index == 0:
            return

        parent_index = self.parent(index)
        if self.heap[index] < self.heap[parent_index]:
            self.swap(index, parent_index)
            self.heapify_up(parent_index)

    def heapify_down(self, index):
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.heapify_down(smallest)

    def insert(self, item):
        self.heap.append(item)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None

        self.swap(0, len(self.heap) - 1)
        min_item = self.heap.pop()
        self.heapify_down(0)
        return min_item
heap = MinHeap()
heap.insert(5)
heap.insert(11)
heap.insert(-1)

heap.insert(-3)
heap.insert(8)
heap.insert(1)
heap.insert(10)
print(heap.heap)
min_item = heap.extract_min()
print(min_item)  # Output: 1

min_item = heap.extract_min()
print(min_item)  # Output: 3
print(heap.heap)