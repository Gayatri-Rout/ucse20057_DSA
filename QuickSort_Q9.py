# ucse20057 | Gayatri Rout | DSA assignment 
# swapping function
def swap(ary, x, y):
    ary[x], ary[y] = ary[y], ary[x]
# Quick Sort
def quickSort(ary):
    if len(ary) == 0:
        return ary
    else:
        pivot = ary[0]
        i = 0
        new_size = len(ary) - 1

        for j in range(new_size):
            if ary[j+1] < pivot:
                swap(ary, j+1, i+1)
                i = i + 1

        swap(ary, 0, i)
        # partitioning and sorting / divide and conquer
        fhalf = quickSort(ary[:i])
        shalf = quickSort(ary[i+1:])
        fhalf.append(ary[i])
        return fhalf + shalf
    
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

if new_size == 1:
    print("\nSorted array:", end=" ") # one element array is already sorted
    print(ary)
else: 
    result = quickSort(ary)
    print("\nSorted array:", end=" ")
    print(result)
