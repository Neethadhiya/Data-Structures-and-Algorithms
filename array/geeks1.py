# An array contains both positive and negative numbers in random order. Rearrange the array elements so that
# positive and negative numbers are placed alternatively. A number of positive and negative numbers need not 
# be equal. If there are more positive numbers they appear at the end of the array. If there are more negative
# numbers, they too appear at the end of the array.
# For example, if the input array is [-1, 2, -3, 4, 5, 6, -7, 8, 9], then the output should
#  be [9, -7, 8, -3, 5, -1, 2, 4, 6]
def quicksort(a):
    if len(a)<=1:
        return a
    else:
        less = []
        greater = []
        pivot = a[0]
        for i in a[1:]:
            if i>pivot:
                greater.append(i)
            else:
                less.append(i)
        return quicksort(less)+[pivot]+quicksort(greater)
a= [-1, 2, -3, 4, 5, 6, -7, 8, 9]
a=quicksort(a)
print("result",a)
i=0
n=len(a)
while a[i]<0:
    temp=a[n-1]
    a[n-1]=a[i]
    a[i]=temp
    i+=2
print("lateest",a)

