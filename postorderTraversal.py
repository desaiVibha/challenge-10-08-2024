# Postorder traversal visits the node in the order: Left -> Right -> Root

# Algorithm for Postorder Traversal:

# 1. Traverse the left subtree, i.e., call Postorder(left->subtree)
# 2. Traverse the right subtree, i.e., call Postorder(right->subtree)
# 3. Visit the root

# Uses of Postorder Traversal:

# 1. Postorder traversal is used to delete the tree. See the question for the deletion of a tree for details.
# 2. Postorder traversal is also useful to get the postfix expression of an expression tree.
# 3. Postorder traversal can help in garbage collection algorithms, particularly in systems where manual memory management is used.

class Node:
    # Constructor to create a new node
    def __init__(self, data):
        # Assign data to this node
        self.data = data
        # Initialize left and right children as None
        self.left = None
        self.right = None

# Function to perform postorder traversal
def postorderTraversal(node):
    # Base case: if the current node is null, return
    if node is None:
        return
    # Recur on the left subtree
    postorderTraversal(node.left)
    # Recur on the right subtree
    postorderTraversal(node.right)
    # Visit the current node
    print(node.data, end=' ')

# Main function
def main():
    # Creating the tree nodes
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    # Perform postorder traversal
    print("Postorder traversal: ", end='')
    postorderTraversal(root)
    print()

# Run the main function
if __name__ == "__main__":
    main()