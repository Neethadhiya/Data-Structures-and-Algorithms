a=[1,2,4,6]
# a.append("vv")
# print(a)
# a.insert(1,"pp")
# print(a)
# b=[99,000]
# a.extend(b)
# print(a)
# b=(888,999)
# a.extend(b)
# print(a)
# b={1:"jjj",755:"ijol"}
# a.extend(b)
# print(a)
# a.remove()
a=["one","two","three","four","five"]
# a.remove("three")
# print(a)
# a.pop(2)
# print(a)
# a.pop()
# print(a)
# del a[2]
# print(a)
# del a
# print(a)
# a.clear()
# print(a)
# for  i in a:
#     print(i)
a=["one","two","three","four","five"]
# for i in range(len(a)):
#     print(a[i])
# i=0
# while i<len(a):
#     print(a[i])
#     i +=1
# b=[print(i) for i in a]
# a=879898
# b=[int(i) for i in str(a)]
# print(b)
# a=[2,4,5,6,7,7]
# b=int(''.join(map(str,a)))
# print(b)
# print(type(b))
a=["one","two","three","four","five","zero"]
# b=[x for x in a if "t" in x]
# print(b)
# a=[x for x in range(6) if x%2==0]
# print(a)
# b=[print(x.upper()) for x in a]
# b=[print(x.capitalize()) for x in a]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a=[1,2,3,4,5,6]
# def myfun(n):
#     return abs(n-1)
# a.sort(key=myfun)
# print(a)
# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

# a=[77,99,67,90]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
a=["ane","Bwo","Shree","Cour","Five","zero"]
# a.sort()
# print(a)
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
# a.sort(key=str.lower)
# print(a)
# b=list(a)
# print(b)
# b=[9,77,5]
# print(a+b)
# a.extend(b)
# print(a)
# for x in b:
#     a.append(x)
# print(a)
b=(2,3,4,67,7)
# if 2 in b:
#     print("yes")
# b=list(b)
# b[1]=000
# b=tuple(b)
# print(b)
# a=("gg",)
# c=a+b
# print(c)
# a=("jj","kk","ui",1,2,3)
# # [x,y,z]=a
# # print(x,y,z)
# [x,*y,z]=a
# print(x,y,z)
# a=[2,6,9]
# print(a*3)
# b={"hh","hh","jj","ii","ii"}
# print(b)
# for i in b:
#     print(i)
# b.add("oooo")
# print(b)
# b.remove("oooo")
# print(b)
# a=["hh","kk","ll"]
# a=set(a)
# b=["kk","oo","yy"]
# b=set(b)
# c=a.symmetric_difference_update(b)
# print(c)
# class Tree:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#     def insert(self,data):
#         if data<self.data:
#             if self.left is None:
#                 self.left=Tree(data)
#             else:
#                 self.left.insert(data)
#         else:
#             if self.right is None:
#                 self.right=Tree(data)
#             else:
#                 self.right.insert(data)
#     def preorder_traversal(self):
#         if self.left is not None:
#             self.left.preorder_traversal()
#         elif self.right is not None:
#             self.right.preorder_traversal()
#         print(self.data)
# tree=Tree(22)
# tree.insert(8)
# tree.insert(9)
# tree.insert(90)
# tree.preorder_traversal()

# a={2,88,99,22}
# a.add("jj")
# print(a)
# b={999,777,555}
# a.update(b)
# print(a)
# a.discard(999)
# a={6767,98798}
# b={6767,98798,68768,77}
# # z=a.isdisjoint(b)
# # print(z)
# print(b.issuperset(a))
a={"name":"Neetha","age":88,"place":"calicut"}
print(a["name"])
print(len(a))
b=dict(name="Neetha",age=88,place="calicut")
print(b.get("name"))
print(b.keys())      

