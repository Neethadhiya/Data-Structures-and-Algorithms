a=[2,4,1,44,22,4,12]
count=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
for i in range(len(a)):
    isPrime=0
    if a[i]<2:
        isPrime=1
    for j in range(2,a[i]//2+1):
        if a[i]%j==0:
            isPrime=1
            break
    if isPrime==0:
        print(a[i])
        count+=1
print(count,'count')