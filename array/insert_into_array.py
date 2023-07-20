# a=[1,2,3,4,5]
# def insert_into_array(a,index,num):
#     a.append(None)
#     for i in range(len(a)-1,index-1,-1):
#         a[i]=a[i-1]
#     a[index-1]=num

# insert_into_array(a,3,44)
# print(a)

# insert at the end
a=[1,2,3,4,5,6]
def insert_at_end(a,num):
    a.append(None)
    print(len(a))
    for i in range(len(a)):
        a[len(a)-1]=num
insert_at_end(a,88)
print(a)