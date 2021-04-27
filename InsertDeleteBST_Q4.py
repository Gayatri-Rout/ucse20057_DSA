# ucse20057 | Gayatri Rout | DSA assignment 
# Insert into and Delete from Binary Search Tree
class Node:
    def __init__(node, data):

        node.left = None
        node.right = None
        node.data = data

    # function to insert node into BST
    def insert(node, data):
        if node.data:
            if data < node.data:
                if node.left == None:
                    node.left = Node(data)
                else:
                    node.left.insert(data)
            elif data > node.data:
                if node.right == None:
                    node.right = Node(data)
                else:
                    node.right.insert(data)
        else:
            node.data = data
    
    # function to display BST after insertion of node
    def insertDisplay(node):
        if node.left:
            node.left.insertDisplay()
        print(node.data, end = " ")
        if node.right:
            node.right.insertDisplay()

# function to display BST after deletion of node
def delDisplay(root):
    if root != None:
        delDisplay(root.left)
        print(root.data, end=" ")
        delDisplay(root.right)

# function to find min data value
def minData(node):
    current = node
    while(current.left is not None):
        current = current.left
 
    return current

# function to delete a node from BST
def delete(root, key):
 
    # key is not found 
    if root is None:
        print("{0} DOESN'T EXIST!" .format(key))
        return root
 
    # key is less than root data, visit left subtree
    if key < root.data:
        root.left = delete(root.left, key)
 
    # key is greater than root data, visit right subtree
    elif(key > root.data):
        root.right = delete(root.right, key)
 
    else:
 
        # node has only one or no child
        if root.left == None:
            temp = root.right
            root = None
            return temp
 
        elif root.right == None:
            temp = root.left
            root = None
            return temp
 
        # node has two children, so getting inorder successor
        temp = minData(root.right)
        root.key = temp.data
        root.right = delete(root.right, temp.data) 
 
    return root

# list of numbers to craete BST from
n_list = [34, 28, 12, 15, 78, 5, 13, 90, 52, 8]
root = Node(n_list[0])
size = len(n_list)
for n in range(1, size):
    root.insert(n_list[n])

# Inserting nodes & deleting nodes: user input
while n != 3:
    n = int(input("\n\nInsert(press 1)\nDelete(press 2)\nQuit(press 3)\n\nWhat to do? "))
    if n == 1:
        insert_node = int(input("Node value to insert? "))
        root.insert(insert_node)
        print("\nBST after Insertion of {0}: " .format(insert_node))
        root.insertDisplay()
    elif n == 2:
        print("Last updated: ", end = " ")
        root.insertDisplay()
        del_node = int(input("\nNode value to delete? "))
        delete(root, del_node)
        print("\nBST after Deletion of {0}: " .format(del_node))
        delDisplay(root)
    else:
        print("\nIncorrect Input!\nTRY AGAIN")

print("\n------------PROGRAM TERMINATED :)------------\n")