a=[1,2,3,4,5,6,1,1,1,2,2]
b=9
count=0
c=0
for i in range(len(a)):
    count=0
    for j in range(len(a)):
        if i!=j:
            if a[i]==a[j]:
                count+=1
    
    if count==0:
        print(a[i])
        c+=1
print("count",c)
        
    
    