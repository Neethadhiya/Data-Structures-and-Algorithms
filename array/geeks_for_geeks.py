# Given an array of elements of length N, ranging from 0 to N – 1. All elements may not be present in the array. If the element is not present then there will be -1 present in the array. Rearrange the array such that A[i] = i and if i is not present, display -1 at that place.

# Examples: 

# Input : arr = {-1, -1, 6, 1, 9, 3, 2, -1, 4, -1}
# Output : [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]

# Input : arr = {19, 7, 0, 3, 18, 15, 12, 6, 1, 8,
#               11, 10, 9, 5, 13, 16, 2, 14, 17, 4}
# Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#          11, 12, 13, 14, 15, 16, 17, 18, 19]
# def fixArray(ar, n):
     
#     # Iterate over the array
#     for i in range(n):
#         for j in range(n):
 
#             # Check is any ar[j]
#             # exists such that
#             # ar[j] is equal to i
#             if (ar[j] == i):
#                 ar[j], ar[i] = ar[i], ar[j]
 
#     # Iterate over array
#     for i in range(n):
         
#         # If not present
#         if (ar[i] != i):
#             ar[i] = -1
 
#     # Print the output
#     print("Array after Rearranging")
 
#     for i in range(n):
#         print(ar[i], end = " ")
 
# # Driver Code
# ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
# n = len(ar)
 
# # Function Call
# fixArray(ar, n)
ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
n = len(ar)
for i in range(n):
    for j in range(n):
        if i==ar[j]:
            ar[j], ar[i] = ar[i], ar[j]
print(ar)
