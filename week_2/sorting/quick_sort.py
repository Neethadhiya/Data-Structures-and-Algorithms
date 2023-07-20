# def quicksort(a):
#     if len(a)<=1:
#         return a
#     else:
#         less=[]
#         greater=[]
#         pivot=a[0]
#         for x in a[1:]:
#             if x<=pivot:
#                 less.append(x)
#             else:
#                 less.append(x)
#     return quicksort(less)+[pivot]+quicksort(greater)
# a=[4,2,7,44,1,33,23,54,65]
# print(quicksort(a))
def quick_sort(a):
    if len(a)<=1:
        return a
    else:
        pivot=a[0]
        less=[]
        greater=[]
        for i in a[1:]:
            if i<=pivot:
                less.append(i)
            else:
                greater.append(i)
    return quick_sort(less)+[pivot]+quick_sort(greater)

a=[22,8,2,1,0,33,55,2]
print(quick_sort(a))