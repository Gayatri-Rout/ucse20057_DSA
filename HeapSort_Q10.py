# ucse20057 | Gayatri Rout | DSA assignment
# swapping function
def swap(ary, x, y):
    ary[x], ary[y] = ary[y], ary[x]

# Heapify function: maintaining max-heap
def heapify(ary,size, i): # i = non-leaf node
    # initializing left & right child nodes
    left = 2*i
    right = 2*i + 1
    
    # setting root as max value
    largest = i
    
    # compare root with left child to find max amongst them
    if ((left < size) and ary[left] > ary[i] ):
        largest = left
        
    # compare current largest with right child to find max amongst them
    if ((right < size) and ary[right] > ary[largest] ):
        largest = right
        
    # changing the root and maintaining heap property
    if largest != i:
        swap(ary, i, largest)
        heapify(ary, size, largest)
    
        
# BuildHeap function: building max-heap
def buildHeap(ary):
    n = size//2 # first non-leaf node
    for i in range(n, -1, -1):
        heapify(ary, size, i)
    
# HeapSort: finally sorting the array
def heapSort(ary):
    buildHeap(ary) # max heap
    
    # deleting elements one by one
    for j in range(size-1, 0, -1):
        swap(ary, j, 0)
        heapify(ary, j,  0)
        
    
# Obtaining the array to be sorted
ary = []
size = int(input("Size of array? "))
for i in range(1, size+1):
    ary.append(int(input("Enter element {0}: " .format(i))))

print("\nOriginal array:", end=" ")
print(ary)
if size == 1 or size == 0:
    print("\nSorted array:", end=" ") # one element array is already sorted
    print(ary)
else: 
    heapSort(ary)
    print("\nSorted array:", end=" ")
    print(ary)