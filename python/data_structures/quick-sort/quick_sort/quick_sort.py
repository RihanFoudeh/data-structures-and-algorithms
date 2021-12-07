def quick_sort(arr, left, right):

    if not arr:
        return "This is an empty array !"

    if left < right:

        position = partition(arr, left, right)
        quick_sort(arr, left, position - 1)
        quick_sort(arr, position + 1, right)
        return arr


def partition(arr, left, right):
    pivot = arr[right]
    low = left - 1
    for i in range(left, right):
        if arr[i] <= pivot:
            low += 1
            Swap(arr, i, low)
    Swap(arr, right, low + 1)
    return low + 1



def Swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


if __name__ == "__main__":
    arr1 = [8, 4, 23, 42, 16, 15]
    arr1 = quick_sort(arr1, 0, len(arr1) - 1)
    print(f"Array Sort [8, 4, 23, 42, 16, 15]:          {arr1}")

    arr2 = [20, 18, 12, 8, 5, -2]
    arr2 = quick_sort(arr2, 0, len(arr2) - 1)
    print(f"Reverse-sorted: [20, 18, 12, 8, 5, -2]:     {arr2}")

    arr3 = [5, 12, 7, 5, 5, 7]
    arr3 = quick_sort(arr3, 0, len(arr3) - 1)
    print(f"Few uniques: [5, 12, 7, 5, 5, 7]:           {arr3}")

    arr4 = [8, 4, 23, 42, 16, 15]
    arr4 = quick_sort(arr4, 0, len(arr4) - 1)
    print(f"Nearly-sorted: [2, 3, 5, 7, 13, 11]:        {arr4}")

    arr5 = []
    arr5 = quick_sort(arr5, 0, len(arr5) - 1)
    print(f"Empty array: []:                            {arr5}")
