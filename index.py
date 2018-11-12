def binary_search(arr, val, start, end):
    #figure out whether we should insert before or after the left boundary
    if start == end: 
        if arr[start] > val:
            return start
        else: 
            return start+1

    # this occurs if we are moving beyond left's boundary making the left boundary the least position to find a number greater than val
    if start > end: 
        return start

    # get the middle of the array
    mid = (start+end) / 2
    # see if the middle is greater or less than val (or equal)
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val: 
        return binary_search(arr, val, start, mid-1)
    else: 
        return mid

#insertion sort
def insertion_sort(arr): 
    for i in xrange(1, len(arr)): 
        val = arr[i] 
        j = binary_search(arr, val, 0, i-1) 
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:] 
    return arr 
  
print("Sorted array:") 
insertion_sort_value = insertion_sort([37, 23, 0, 17, 12, 72, 31, 
                        46, 100, 88, 54]) 
print(insertion_sort_value)
