# a=[2,5,22,1,55,6,3,20]
# i=0
# j=1
# for i in range(len(a)):
#     for j in range(len(a)-i):
#         if a[j]>a[j+1]:
#             temp=a[j]
#             a[j]=a[j+1]
#             a[j+1]=temp
#     print(a)
# print(a)

# def bubble_sort(arr):
#     for i in range(len(arr)):
#         for j in range(len(arr)-1 - i):
#             if arr[j] > arr[j + 1]:
#                 temp=arr[j]
#                 arr[j]=arr[j+1]
#                 arr[j+1]=temp
# arr = [2, 5, 22, 1, 55, 6, 3, 20]
# bubble_sort(arr)
# print(arr)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1-i):
            if a[j+1]<a[j]:
                temp=a[j+1]
                a[j+1]=a[j]
                a[j]=temp
    return a
a=[89,4,2,7,44,2,78,440]
print(bubble_sort(a))