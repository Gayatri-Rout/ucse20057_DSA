# ucse20057 | Gayatri Rout | DSA assignment 
# Implementing 3 traversal techniques on Binary Tree: In/Pre/Post order
class Node:
    def __init__(node, data):

        node.left = None
        node.right = None
        node.data = data

    # function to display Inorder tree traversal
    def displayInorder(node):
        if node.left:
            node.left.displayInorder()
        print(node.data, end = " ")
        if node.right:
            node.right.displayInorder()
    
    # function to display Preorder tree traversal
    def displayPreorder(node):
        print(node.data, end = " ")
        if node.left:
            node.left.displayPreorder()        
        if node.right:
            node.right.displayPreorder()
    
    # function to display Postorder tree traversal
    def displayPostorder(node):
        if node.left:
            node.left.displayPostorder()
        if node.right:
            node.right.displayPostorder()
        print(node.data, end = " ")

# create binary tree
root = Node(13)
root.left = Node(56)
root.right = Node(39)
root.left.left = Node(23)
root.left.left.left = Node(76)
root.left.left.right = Node(21)
root.left.right = Node(34)

# Printing Binary Tree
print("\nIn-order (Left -> Root -> Right): ")
root.displayInorder()
print("\nPre-order (Root -> Left -> Right): ")
root.displayPreorder()
print("\nPost-order (Left -> Right -> Root): ")
root.displayPostorder()
