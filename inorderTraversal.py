# Inorder traversal visits the node in the order: Left -> Root -> Right

# Algorithm for Inorder Traversal:
# 1. Traverse the left subtree, i.e., call Inorder(left->subtree)
# 2. Visit the root.
# 3. Traverse the right subtree, i.e., call Inorder(right->subtree)
# Uses of Inorder Traversal:
# 1. In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
# 2. To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.
# 3. Inorder traversal can be used to evaluate arithmetic expressions stored in expression trees.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform inorder traversal
def inorderTraversal(root):  
    # Base case: if null
    if root is None:
        return      
    # Recur on the left subtree
    inorderTraversal(root.left)    
    # Visit the current node
    print(root.data, end=" ")    
    # Recur on the right subtree
    inorderTraversal(root.right)
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
inorderTraversal(root)