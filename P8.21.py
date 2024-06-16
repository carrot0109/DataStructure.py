class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def check_height_and_balance(node):
    if not node:
        return 0, True
    
    left_height, left_balanced = check_height_and_balance(node.left)
    right_height, right_balanced = check_height_and_balance(node.right)
    
    current_height = max(left_height, right_height) + 1
    current_balanced = abs(left_height - right_height) < 2

    return current_height, left_balanced and right_balanced and current_balanced

def is_balanced(root):
    _, balanced = check_height_and_balance(root)
    return balanced

# Example usage:
# Constructing a balanced binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(is_balanced(root))  # Output: True

# Constructing an unbalanced binary tree
#         1
#        / \
#       2   3
#      / 
#     4   
#    /   
#   5   

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(5)

print(is_balanced(root))  # Output: False