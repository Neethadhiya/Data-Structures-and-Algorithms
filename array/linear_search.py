def linear_search(list1,num):
    for i in range(len(list1)):
        if list1[i]==num:
            return i+1
    return -1
list1=[10,22,12,13,24]
num=10
result=linear_search(list1,num)
if result==-1:
    print("the number is not in the list ")
else:
    print("the position is",result)

# l=list()
# n=int(input("enter the size of array"))
# for i in range(n):
#     print("enter the element")
#     l.append(int(input()))
# print(l)


# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i  # Return the index if the target is found
#     return -1  # Return -1 if the target is not found

# # Example usage:
# numbers = [4, 2, 8, 5, 1, 9]
# target_number = 5
# result = linear_search(numbers, target_number)

# if result != -1:
#     print(f"Target number {target_number} found at index {result}.")
# else:
#     print("Target number not found.")
