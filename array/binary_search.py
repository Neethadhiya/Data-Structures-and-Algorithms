def binary_search(a,num):
    low=0
    high=len(a)-1
    mid=0
    found=False
    while(low<=high):
        mid=(low+high)//2
        if a[mid]==num:
            found=True
            print("number found at position",mid+1)
            break
        elif a[mid]>num:
            high=mid-1
        elif a[mid]<num:
            low=mid+1
    if not found:
        print("number not found")
    
a=[1,2,3,4,6,8,9]
key=8
binary_search(a,key)

