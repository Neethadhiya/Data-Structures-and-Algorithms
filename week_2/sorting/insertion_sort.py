# def insertion_sort(a):
#     for i in range(len(a)):
#         if i>0:
#             for j in range(0,i):
#                 print(a[j])
#                 if j>0:
#                     if a[j]<a[j+1]:
#                         print("kkk")
#                         temp=a[i]
#                         a[j]=a[j+1]
#                         a[j+1]=temp
#                     print(a)
#         return a

# a=[2,5,1,7,3,9]
# # print(insertion_sort(a),"lll")
# def insertion_sort(a):
#     for i in range(1,len(a)):
#         key=a[i]
#         j=i-1
#         while j>=0 and key<a[j]:
#             a[j+1]=a[j]
#             j-=1
#         a[j+1]=key
#     return a
# a=[10,1,22,2,11,67,9]
# print(insertion_sort(a))

def insertion_sort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        if key<a[j]:
            while j>=0 and key<a[j]:
                a[j+1]=a[j]
                j-=1
            a[j+1]=key
    return a
a=[88,5,5,2,1,87,3,2]
print(insertion_sort(a))