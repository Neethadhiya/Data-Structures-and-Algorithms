# a=[10,7,-9,44,22,33,1]
# def selection_sort(a):
#     for i in range(len(a)):
#         min_index=i
#         for j in range(i+1,len(a)-1):
#             if a[j]<a[i]:
#                 min_index=j
#         a[i],a[min_index]=a[min_index],a[i]
#     return a
# print(selection_sort(a))

def selection_sort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[j]<a[i]:
                min_index=j
        temp=a[i]
        a[i]=a[min_index]
        a[min_index]=temp
    return a
a=[33,2,3,4,5,4,2,1]
print(selection_sort(a))