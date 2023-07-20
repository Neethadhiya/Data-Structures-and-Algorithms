# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class LinkedListStack:
#     def __init__(self):
#         self.head=None
#     def is_empty(self):
#         return self.head is None
#     def push(self,data):
#         new_node=Node(data)
#         new_node.next=self.head
#         self.head=new_node
#     def pop(self):
#         if self.is_empty():
#             print("Stack is empty")
#             return 
#         popped_data=self.head.data
#         self.head =self.head.next
#         return popped_data
#     def peek(self):
#         if self.is_empty():
#             print("Stack is empty")
#         return self.head.data
#     def display(self):
#         if self.is_empty():
#             print("Stack is empty")
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# list=LinkedListStack()
# list.push(100)
# list.push(88)
# list.push(78)
# list.push(56)
# list.display()
# popped_num=list.pop()
# print("poped number",popped_num)
# list.display()
# print("The top element is ",list.peek())


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self,size):
        self.size=size
        self.head=None

    def is_empty(self):
        return self.head is None
    def push(self,num):
        if self.head is None:
            self.head=Node(num)
        else:
            new_node=Node(num)
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.next=None
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            popped_data=self.top
            self.top=self.top.next
            self.size-=1
            return popped_data
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current=self.head
            while current:
                print(current.data)
                current=current.next
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current=self.head
            while current.next:
                current=current.next
        return current.data
stack=Stack(10)
stack.push(11)
stack.push(12)
stack.push(16)
stack.display()
stack.pop()
stack.display()
print("top element=",stack.peek())



