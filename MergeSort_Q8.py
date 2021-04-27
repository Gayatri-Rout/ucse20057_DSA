# ucse20057 | Gayatri Rout | DSA assignment 
# merge function: merges the sub-arrays i.e left part & right part of given array
def merge(ary, left, mid, right):
    # length of left & right part of ary
    length_left = mid - left + 1
    length_right = right - mid

    # empty arrays: L[0..length_left] and R[0..length_right]
    L = [0] * (length_left + 1)
    R = [0] * (length_right + 1)

    # copying left part of ary to L[0..length_left]
    for i in range(0, length_left):
        L[i] = ary[left + i]

    # copying right part of ary to R[0..length_right]
    for j in range(0, length_right):
        R[j] = ary[mid + 1 + j]

    # infinity at end of sub-arrays; easier sorting
    positive_infnity = float('inf')
    L[length_left] = positive_infnity
    R[length_right] = positive_infnity

    # copying smallest of L & R to ary
    i = 0
    j = 0
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            ary[k] = L[i]
            i += 1
        else:
            ary[k] = R[j]
            j += 1

# Merge Sort
def mergeSort(ary, low, high):
    
    if low < high:
        mid = (low + high) // 2 # mid index
        mergeSort(ary, low, mid) # sorting left part of ary
        mergeSort(ary, mid + 1, high) # sorting right part of ary
        merge(ary, low, mid, high) # merging the sorted sub-arrays of ary

# Obtaining the array to be sorted
ary = []
size = int(input("Size of array? "))
for i in range(1, size+1):
    ary.append(int(input("Enter element {0}: " .format(i))))

print("\nOriginal array:", end=" ")
print(ary)
# removing duplicates if any
ary = list(set(ary))
print("\nOriginal array (w/o duplicates):", end=" ")
print(ary)
new_size = len(ary) # size of ary after removing duplicates

if new_size == 1 or new_size == 0:
    print("\nSorted array:", end=" ") # one element array is already sorted
    print(ary)
else: 
    mergeSort(ary, 0, new_size-1)
    print("\nSorted array:", end=" ")
    print(ary)
