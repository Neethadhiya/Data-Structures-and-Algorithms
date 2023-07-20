a=[11,22,3,4,5,6,7,0,-9]
small=a[0]
for i in range(1,len(a)):
    if a[i]<small:
        small=a[i]
print(small)