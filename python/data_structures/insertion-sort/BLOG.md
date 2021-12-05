# Insertion Sort

### Insertion Sort is a sorting algorithm in the same family as bubble sort and selection sort. Insertion sort works by iterating across the array starting at the front and comparing if the value of the element next to it is lower. If the next door value is lower the elements change places.

## Pseudocode
```
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
```


# Trace

## Pass 1
```
ary = [8, 4, 23, 42, 16, 15]

j = 0
temp = 4

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[1] = 8
j = -1
ary_sort[0] = 4

ary = [4, 8, 23, 42, 16, 15]
```


 * We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

## Pass 2
```
ary = [8, 4, 23, 42, 16, 15]

j = 1
temp = 23

# Check the while condition
while j >=0 and temp < ary_sort[j]:
    flase

# The ary will stay the same
ary = [4, 8, 23, 42, 16, 15]
```


* The second pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 8 is the 2nd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.


## Pass 3
```
ary = [8, 4, 23, 42, 16, 15]

j = 2
temp = 42

# Check the while condition
while j >=0 and temp < ary_sort[j]:
    flase

# The ary will stay the same
ary = [4, 8, 23, 42, 16, 15]
```


* The third pass through evaluates the remaining indexes in the array, starting at position 2. Both position 4 and 5 are smaller than the value in position 2. Each time a smaller number than the current minimum is found, the variable will update to the new smallest number. In this case, 15 is the next smallest number. As a result, it will swap with position 2.

## Pass 4
```
ary = [8, 4, 23, 42, 16, 15]

j = 3
temp = 16

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[4] = 42
j = 2
ary_sort[3] = 16

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[3] = 23
j = 1
ary_sort[2] = 16


ary = [4, 8, 16, 23, 42, 15]
```


* The 4th pass through on the array proves that 16 is the next smallest number in the array, and as a result, switches places with the 42.

## Pass 5
```
ary = [8, 4, 23, 42, 16, 15]

j = 4
temp = 15

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[5] = 42
j = 3
ary_sort[4] = 15

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[4] = 23
j = 2
ary_sort[3] = 15

# Check the while condition
while j >=0 and temp < ary_sort[j]:
ary_sort[j + 1] = ary_sort[j]
ary_sort[3] = 16
j = 1
ary_sort[2] = 15

# Check the while condition
while j >=0 and temp < ary_sort[j]:
    false

ary = [4, 8, 15, 16, 23, 42]
```


* The 5th pass through of the array only has one other index to evaluate. Since the last index value is larger than index 4, the two values will swap.


## Pass 6
```
ary = [8, 4, 23, 42, 16, 15]

j = 5
temp = 42

# Check the while condition
while j >=0 and temp < ary_sort[j]:
    false

# The ary will stay the same
ary = [4, 8, 15, 16, 23, 42]
```


* On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.
After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.

# Efficency

* Time: `O(n^2)`
    - The basic operation of this algorithm is comparison. This will happen n * (n-1) number of times…concluding the algorithm to be n squared.
* Space: `O(1)`
    - No additional space is being created. This array is being sorted in place…keeping the space at constant O(1).
    
