class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class Hashtable:
    def __init__(self,size):
        self.size=size
        self.hashtable=[None]*size
    def hash_function(self,key):
        return hash(key)%self.size
    def set(self,key,value):
        index=self.hash_function(key)
        if self.hashtable[index] is None:
            self.hashtable[index]=Node(key,value)
        else:
            current=self.hashtable[index]
            while current.next and current.key!=key:
                current=current.next
            if current.key==key:
                current.value=value
            else:
                current.next=Node(key,value)
    def get(self):
        for i in range(len(self.hashtable)):
            node=self.hashtable[i]
            while node:
                print(node.key,'=',node.value)
                node=node.next
table=Hashtable(10)
table.set("apple",8)
table.set("mango",7)
table.set("orange",9)
table.get()

