def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  # Choosing the first element as pivot
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example
arr = [9,23,32,14,38]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)