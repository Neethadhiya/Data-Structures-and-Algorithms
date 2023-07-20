class CircularQueue:
    def __init__(self, k):
        self.size = k
        self.queue = [None] * k
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full. Enqueue operation not allowed.")
        elif self.is_empty():
            self.front = self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Dequeue operation not allowed.")
            return None
        elif self.front == self.rear:
            value = self.queue[self.front]
            self.front = self.rear = -1
            return value
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return value

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:")
            i = self.front
            while i != self.rear:
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print(self.queue[i])


# Example usage:
queue = CircularQueue(5)
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.display()  # Output: Queue: 1 2 3
queue.dequeue()
queue.display()  # Output: Queue: 2 3
