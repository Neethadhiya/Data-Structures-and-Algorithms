a=[1,2,3,4,5,6,2,1,2,1,2,4,5]
b=[]
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if a[i]==a[j]:
            count+=1

    if count==2:
        if a[i] not in b:
            b.append(a[i])

print(b)