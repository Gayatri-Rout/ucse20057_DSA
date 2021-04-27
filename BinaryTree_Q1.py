# ucse20057 | Gayatri Rout | DSA assignment 
# Create and Print binary tree
class Node:
    def __init__(node, data):

        node.left = None
        node.right = None
        node.data = data

    # function to display Binary tree 
    def display(node):
        if node.left:
            node.left.display()
        print(node.data, end = " ")
        if node.right:
            node.right.display()

# create binary tree
root = Node(13)
root.left = Node(56)
root.right = Node(39)
root.left.left = Node(23)
root.left.left.left = Node(76)
root.left.left.right = Node(21)
root.left.right = Node(34)

# Printing Binary Tree
print("\nBinary Tree (Left -> Root -> Right): ")
root.display()
