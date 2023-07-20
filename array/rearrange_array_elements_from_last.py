# Given a sorted array of positive integers, rearrange the array alternately i.e first element should be a maximum value, at second position minimum value, at third position second max, at fourth position second min, and so on. 

# Examples: 

# Input: arr[] = {1, 2, 3, 4, 5, 6, 7} 
# Output: arr[] = {7, 1, 6, 2, 5, 3, 4}

# Input: arr[] = {1, 2, 3, 4, 5, 6} 
# Output: arr[] = {6, 1, 5, 2, 4, 3} 

arr= [1, 2, 3, 4, 5, 6, 7]
small=0
large=len(arr)-1
temp=len(arr)*[None]
flag=True
for i in range(len(temp)):
    if flag==True:
        temp[i]=arr[large]
        large-=1
    else:
        temp[i]=arr[small]
        small+=1
    fla



    

