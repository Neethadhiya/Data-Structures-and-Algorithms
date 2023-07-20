def heapify(a,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left<n and a[largest]<a[left]:
        largest = left
    if right<n and a[largest]<a[right]:
        largest = right 
    if i!=largest:
        a[i],a[largest]=a[largest],a[i]
        heapify(a,n,largest)
def heap_sort(a):
    n = len(a)
    for i in range(n//2-1,-1,-1):
        heapify(a,n,i)
    for i in range(n-1,0,-1):
        a[0],a[i] = a[i],a[0]
        heapify(a,i,0)
a=[29,3,3,4,5,6,789,2]
heap_sort(a)
for i in range(len(a)):
    print(a[i])