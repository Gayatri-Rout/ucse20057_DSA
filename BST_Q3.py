# ucse20057 | Gayatri Rout | DSA assignment 
# Create and Print Binary Search Tree
class Node:
    def __init__(node, data):

        node.left = None
        node.right = None
        node.data = data

    # function to create Binary Search Tree
    def create(node, data):
        if node.data:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    node.left.create(data)
            elif data > node.data:
                if node.right == None:
                    node.right = Node(data)
                else:
                    node.right.create(data)
        else:
            node.data = data

    # function to display Binary Search Tree
    def display(node):
        if node.left:
            node.left.display()
        print(node.data, end = " ")
        if node.right:
            node.right.display()

# list of numbers to craete BST from
n_list = [34, 28, 12, 15, 78, 5, 13, 90, 52, 8]
root = Node(n_list[0])
size = len(n_list)
for n in range(1, size):
    root.create(n_list[n])

# Printing Binary Search Tree
print("\nBinary Search Tree (Left -> Root -> Right): ")
root.display()