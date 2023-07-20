a=[4,2,76,8,3,9]
sum=0
length=len(a)
for i in range(length):
    sum+=a[i]
if sum>100:
    i=0
    while i<length:
        if a[i]%2==0:
            for j in range(i,length-1):
                a[j]=a[j+1]
            length-=1
        else:
            i+=1
a = a[:length]            
print(a)

# a = [4, 2, 76, 8, 3, 9]
# total_sum = sum(a)

# if total_sum > 100:
#     i = 0
#     length = len(a)
#     while i < length:
#         if a[i] % 2 == 0:
#             for j in range(i, length-1):
#                 a[j] = a[j+1]
#             length -= 1
#         else:
#             i += 1

# a = a[:length]
# print(a)

