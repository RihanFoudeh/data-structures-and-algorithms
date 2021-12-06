def insertion_sort(ary_sort):

    if not ary_sort:
        return "This is an empty array !"

    for i in range(1, len(ary_sort)):
        j = i - 1
        temp = ary_sort[i]
        while j >= 0 and temp < ary_sort[j]:
            ary_sort[j + 1] = ary_sort[j]
            j = j - 1
            ary_sort[j + 1] = temp

    return ary_sort

if __name__=="__main__":
    ary_sort1 = insertion_sort([8, 4, 23, 42, 16, 15])
    print (f"Array Sort [8, 4, 23, 42, 16, 15]:          {ary_sort1}")

    ary_sort2 = insertion_sort([20, 18, 12, 8, 5, -2])
    print (f"Reverse-sorted: [20, 18, 12, 8, 5, -2]:     {ary_sort2}")

    ary_sort3 = insertion_sort([5, 12, 7, 5, 5, 7])
    print (f"Few uniques: [5, 12, 7, 5, 5, 7]:           {ary_sort3}")

    ary_sort4 = insertion_sort([2, 3, 5, 7, 13, 11])
    print (f"Nearly-sorted: [2, 3, 5, 7, 13, 11]:        {ary_sort4}")

    ary_sort5 = insertion_sort([])
    print (f"Empty array: []                             {ary_sort5}")
