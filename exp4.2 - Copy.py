def fractional_knapsack(values, weights, capacity):
    n = len(values)
    ratio = [(values[i]/weights[i], i) for i in range(n)]
    ratio.sort(reverse=True)
    
    max_value = 0
    fractions = [0]*n
    
    for r, i in ratio:
        if weights[i] <= capacity:
            max_value += values[i]
            capacity -= weights[i]
            fractions[i] = 1
        else:
            max_value += values[i] * (capacity / weights[i])
            fractions[i] = capacity / weights[i]
            break
    
    return max_value, fractions

values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_val, item_fraction = fractional_knapsack(values, weights, capacity)
print(f"Maximum value: {max_val}")
print(f"Fractions of items taken: {item_fraction}")

Quick sort code 


def Quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]   # Correct spelling & indexing
    left = [x for x in arr if x < pivot]      # generator () → list []
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return Quick_sort(left) + middle + Quick_sort(right)

numbers = [3, 6, 8, 10, 1, 2, 1]
print("Unsorted:", numbers)
print("Sorted:", Quick_sort(numbers))


Merge sort 

def merge_sort(a):
    if len(a)<2: return a
    m=len(a)//2
    L,R=merge_sort(a[:m]),merge_sort(a[m:])
    i=j=0; out=[]
    while i<len(L) and j<len(R):
        if L[i]<R[j]: out.append(L[i]); i+=1
        else: out.append(R[j]); j+=1
    return out+L[i:]+R[j:]

print(merge_sort([3,6,1,8,4]))
/
/
/

quick sort revision
def 

