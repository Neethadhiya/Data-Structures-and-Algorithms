
# find the pairs who have same characters in the list
# a=["aba","aabb","abcd","bac","aabc"]
# a=["aabb","ab","ba"]
a=["nba","cba","dba"]
pair=0
b=[]
for i in a:
    b.append([set(i)])
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]==b[j]:
            pair+=1
print(pair)
        
