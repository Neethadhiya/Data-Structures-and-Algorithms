class MaxHeap:
    def __init__(self):
        self.heap = []
    def parent_index(self,index):
        return (index-1)//2
    def left_child(self,index):
        return 2*index+1
    def right_child(self,index):
        return 2*index+2
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def insert(self,data):
        self.heap.append(data)
        self.heapify_up(len(self.heap)-1)
    def heapify_up(self,index):
        if index == 0:
            return 
        parent_index = self.parent_index(index)
        if self.heap[index] > self.heap[parent_index]:
            self.swap(index,parent_index)
            self.heapify_up(parent_index)
    def extract_max(self):
        self.swap(0,len(self.heap)-1)
        max_value = self.heap.pop()
        self.heapify_down(0)
        return max_value
    def heapify_down(self,index):
        largest = index
        left = self.left_child(index)
        right = self.right_child(index)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right 
        if index != largest:
            self.swap(index,largest)
            self.heapify_down(largest)
heap = MaxHeap()
heap.insert(1)
heap.insert(2)
heap.insert(23)
heap.insert(21)
heap.insert(28)
heap.insert(33)
heap.insert(0)
heap.insert(23)
print(heap.heap)
max_value = heap.extract_max()
print("max = ",max_value)
print(heap.heap)
