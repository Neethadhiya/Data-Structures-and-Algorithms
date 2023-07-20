class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=None
        self.rear=None
        
        self.size=0
    def is_empty(self):
        return self.front is None  
    def enqueue(self,data):
        new_node=Node(data)
        if self.rear is None:
            self.rear=self.front=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            temp=self.front
            self.front=temp.next
        if self.front==None:
            self.rear=None
        self.size-=1
        return temp
    def display(self):
        if self.front is None:
            print("Queue is empty")
        else:
            current=self.front
            while current is not None:
                print(current.data)
                current=current.next

queue=Queue()
queue.enqueue(11)
queue.enqueue(13)
queue.enqueue(12)
queue.display()

queue.dequeue()
queue.display()