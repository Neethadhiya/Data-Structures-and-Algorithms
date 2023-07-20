# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     # Divide the array into two halves
#     mid = len(arr) // 2
#     left_array = arr[:mid]
#     right_array = arr[mid:]
    
#     # Recursively sort the two halves
#     left_array = merge_sort(left_array)
#     right_array = merge_sort(right_array)
    
#     # Merge the sorted halves
#     sorted_arr = merge(left_array, right_array)
    
#     return sorted_arr


# def merge(left_array, right_array):
#     merged = []
#     left_index = 0
#     right_index = 0
    
#     # Compare and merge elements from both halves
#     while left_index < len(left_array) and right_index < len(right_array):
#         if left_array[left_index] <= right_array[right_index]:
#             merged.append(left_array[left_index])
#             left_index += 1
#         else:
#             merged.append(right_array[right_index])
#             right_index += 1
    
#     # Copy remaining elements, if any
#     # while left_index < len(left_array):
#     #     merged.append(left_array[left_index])
#     #     left_index += 1
#     merged+=left_array[left_index:]    
    
#     # while right_index < len(right_array):
#     #     merged.append(right_array[right_index])
#     #     right_index += 1
#     merged+=right_array[right_index:]
    
#     return merged


# # Example usage
# arr = [5, 2, 9, 1, 7, 6, 4]
# sorted_arr = merge_sort(arr)
# print(sorted_arr)



def merge(left_array,right_array):
    left_index=0
    right_index=0
    merged=[]
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index]<=right_array[right_index]:
            merged.append(left_array[left_index])
            left_index+=1
        else:
            merged.append(right_array[right_index])
            right_index+=1
    merged+=left_array[left_index:]
    merged+=right_array[right_index:]
    return merged

def merge_sort(a):
    if len(a)<=1:
        return a
    mid=len(a)//2
    left_array=a[:mid]
    right_array=a[mid:]
    left_array=merge_sort(left_array)
    right_array=merge_sort(right_array)
    sorted=merge(left_array,right_array)
    return sorted
a=[22,33,2,4,8,3,0,7,1]
print(merge_sort(a))