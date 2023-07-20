a=[2,3,9,10,4,5,6,7,8]
count=0
for i in range(len(a)):
    isPrime=0
    if a[i]<2:
        isPrime=1
    for j in range(2,int(a[i]//2)):
        if a[i]%j==0:
            isPrime=1
            break
    if isPrime==0:
        print(a[i])
        count+=1
print("count=",count)