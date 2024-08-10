# Preorder traversal visits the node in the order: Root -> Left -> Right

# Algorithm for Preorder Traversal:
# 1. Visit the root.
# 2. Traverse the left subtree, i.e., call Preorder(left->subtree)
# 3. Traverse the right subtree, i.e., call Preorder(right->subtree)

# Uses of Preorder Traversal:
# 1. Preorder traversal is used to create a copy of the tree.
# 2. Preorder traversal is also used to get prefix expressions on an expression tree.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to perform preorder traversal
def preorderTraversal(root):  
    # Base case
    if root is None:
        return      
    # Visit the current node
    print(root.data, end=' ')    
    # Recur on the left subtree
    preorderTraversal(root.left)    
    # Recur on the right subtree
    preorderTraversal(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    preorderTraversal(root)