a=[1,2,3,4,5,6,7,8,9,33]
for i in range(len(a)):
    isPrime=0
    isEven=0
    if a[i]<2:
        isPrime=1
    for j in range(2,a[i]//2+1):
        if a[i]%j==0:
            isPrime=1
            break
    if a[i]%2==0:
        a[i]=0
    if isPrime==0:
        a[i]=1
print(a)