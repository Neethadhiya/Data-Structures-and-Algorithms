def binary_search(a,num,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if a[mid]==num:
        print("position",mid+1)
    elif a[mid]>num:
        high=mid-1
        binary_search(a,num,low,high)
    elif a[mid]<num:
        low=low-1
        binary_search(a,num,low,high)
a=[2,3,4,5,6,77,44]
num=5
length=len(a)-1
binary_search(a,num,0,length)