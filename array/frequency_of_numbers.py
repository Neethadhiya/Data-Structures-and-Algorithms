a=[2,1,5,3,4,3,3,4,4,4,2,2,2,6,6,6]
even ={}
count =[]
mini=[]
for i in range(len(a)):
    if a[i]%2==0:
        if a[i] in even:
            even[a[i]] +=1
        else:
            even[a[i]] =1
for key,value in even.items():
    


maxi =max(even.values())
for key,value in even.items():
    if value==maxi:
        count.append(key)
print(min(count))



    
