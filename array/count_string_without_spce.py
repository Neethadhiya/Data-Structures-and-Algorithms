def count_char(a):
    count=0
    for i in range(len(a)):
        if a[i]==' ':
            print("jj",a[i])            
            continue
        
        
        count+=1
    return count
a="hello world"
count=0
for i in range(len(a)):
    count+=1
print("count with space",count)
print("without space",count_char(a))