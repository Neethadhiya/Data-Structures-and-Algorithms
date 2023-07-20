a=[1,3,4]
b=[10,20]
for i in range(len(a)):
    for j in range(len(b)):
        temp=b[j]
        b[j]=a[i]
        a[i]=temp
print("a",a)
print("b",b)