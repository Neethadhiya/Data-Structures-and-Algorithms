class Queue:
    def __init__(self, capacity):
        self.queue = []
        self.front = 0
        self.rear = -1
        self.capacity = capacity

    def is_empty(self):
        return self.rear < self.front

    def is_full(self):
        return self.rear - self.front + 1 == self.capacity

    def enqueue(self, item):
        if self.is_full():
            return "Queue is full"
        else:
            self.rear += 1
            self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            item = self.queue[self.front]
            self.front += 1
            return item

    def front_item(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            return self.queue[self.front]

    def size(self):
        return self.rear - self.front + 1
queue = Queue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print(queue.size())  # Output: 3

print(queue.is_full())  # Output: True

queue.dequeue()
print(queue.is_full())  # Output: False
