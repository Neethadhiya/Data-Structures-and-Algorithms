str="dd332sd"
length=len(str)
for i in range(length):
    flag=0
    if str[i]==str[-i-1]:
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("palindrome")
else:
    print("not palindrome")
    