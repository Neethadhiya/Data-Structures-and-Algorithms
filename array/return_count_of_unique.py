a=[1,2,3,4,3,2,1,1,1]
# num=[]
# for i in range(len(a)):
#     if a[i] in num:
#         continue
#     else:
#         num.append(a[i])
# print(num)
# print(len(num))
nums=[1,1,2,2,1,3,5,6]
j = 0
i=1
length=len(nums)
while length>0:
    if nums[j] == nums[i]:
        nums[j] = nums[i]
        length-=1
        i+=1
        j+=1
    else:
        i+=1
        j+=1


print(nums)