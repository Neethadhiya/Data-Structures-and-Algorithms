a=[0,0,2,0,3,4,0,9,0,9,0]
n=len(a)
for i in range(n):
    if a[i]==0 and a[n-1]!=0:
        temp=a[n-1]
        a[n-1]=a[i]
        a[i]=temp
    elif a[i]==0 and a[n-1]==0:
        for i in range(i,n-1):
            temp1=a[i]
            a[i]=a[i+1]
        a[n-1]=temp1
            
print(a)



