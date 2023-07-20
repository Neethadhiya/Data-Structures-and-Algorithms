class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
class HashTable:
    def __init__(self,size):
        self.size=size
        self.hashtable=[None]*size
    def hash_function(self,key):
        return hash(key)%self.size
    def insert(self,key,value):
        index=self.hash_function(key)
        if self.hashtable[index] is None:
            self.hashtable[index]=Node(key,value)
        else:
            node=self.hashtable[index]
            while node.next is not None and node.key!=key:
                node=node.next
            if node.key==key:
                node.value=value
            else:
                new_node=Node(key,value)
                node.next=new_node
    def delete(self,key):
        index=self.hash_function(key)
        node=self.hashtable[index]
        prev_node=None
        while node is not None:
            if node.key==key:
                if prev_node is None:
                    self.hashtable[index]=node.next
                else:
                    prev_node.next=node.next
                return 
            prev_node=node
            node=node.next
        raise KeyError(key)
    def display(self):
        for i in range(self.size):
            print(f'{i}:',end='')
            node=self.hashtable[i]
            while node is not None:
                print(f'{node.key}={node.value}',end='-->')
                node=node.next
            print("None")
            
            
table=HashTable(5)
table.insert("apple",1)
table.insert("banana","9")
table.insert("papaya",7)
table.display()
table.delete("apple")
table.display()



