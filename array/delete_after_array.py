a=[1,2,3,4,5,9]
def delete_after(a,pos):
    for i in range(pos-1,len(a)-1):
        a[i]=a[i+1]
    a.pop()
    print(a)
delete_after(a,3)