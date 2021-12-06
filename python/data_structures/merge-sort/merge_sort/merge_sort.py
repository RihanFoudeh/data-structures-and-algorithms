def  mergesort(arr):
    length = len(arr)

    if length > 1:
       mid = length // 2
       left = arr[0:mid]
       right = arr[mid:length]
    # sort the left side
       mergesort(left)
    # sort the right side
       mergesort(right)
    # merge the sorted left and right sides together
       merge(left, right, arr)

##################################################################

def merge(left, right, arr):
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1

        k = k + 1

    if i == len(left):
        for x in right[j:]:
            arr[k] = x
            k += 1
    else:
        for x in left[i:]:
            arr[k] = x
            k += 1

if __name__ == "__main__":
    arr1 = [8, 4, 23, 42, 16, 15]
    mergesort(arr1)
    print (f"Array Sort [8, 4, 23, 42, 16, 15]:          {arr1}")

    arr2 = [20, 18, 12, 8, 5, -2]
    mergesort(arr2)
    print (f"Reverse-sorted: [20, 18, 12, 8, 5, -2]:     {arr2}")

    arr3 = [5, 12, 7, 5, 5, 7]
    mergesort(arr3)
    print (f"Few uniques: [5, 12, 7, 5, 5, 7]:           {arr3}")

    arr4 = [8,4,23,42,16,15]
    mergesort(arr4)
    print (f"Nearly-sorted: [2, 3, 5, 7, 13, 11]:        {arr4}")
