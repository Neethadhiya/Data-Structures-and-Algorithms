class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.top=None
        
        self.size=0

    def is_empty(self):
        return self.size==0
    def push(self,data):
        new_node=Node(data)
        if self.top==None:
            self.top=new_node
            new_node.next=None
        else:
            current=self.top
            while current.next is not None:
                current=current.next
            current.next=new_node
        self.size+=1
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        else:
            popped_data=self.top
            self.top=self.top.next
            self.size-=1
            return popped_data
    def display(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current=self.top
            while current:
                print(current.data)
                current=current.next
    def reverse(self):
        if self.top is None:
            print("Stack is empty")
        
        while not self.is_empty():
            temp=self.pop()
            print(temp.data)
            
        
s=Stack()
s.push(22)
s.push(23)
s.push(45)
s.display()
# s.pop()
# s.display()
print("revesed")
s.reverse()



