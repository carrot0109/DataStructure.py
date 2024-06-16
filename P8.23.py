class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mirror_tree(root):
    if not root:
        return None
    
    # 재귀적으로 좌우 자식을 교환
    root.left, root.right = root.right, root.left       # 좌우대칭이니까 무엇이든 다 바꿔버림
    
    # 왼쪽과 오른쪽 서브트리에서도 동일한 작업 수행
    mirror_tree(root.left)
    mirror_tree(root.right)
    
    return root

# Example usage:
# Constructing a binary tree
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

# Mirror the binary tree
mirror_tree(root)

# The mirrored tree should be:
#         1
#        / \
#       3   2
#      /   / \
#     6   5   4

def print_tree(node, level=0, label="."):
    """Helper function to display the tree structure."""
    indent = "   " * level
    print(f"{indent}-{label}: {node.value if node else 'None'}")
    if node:
        if node.left or node.right:  # If there's any child, print the children
            print_tree(node.left, level + 1, "L")
            print_tree(node.right, level + 1, "R")

# Display the mirrored tree
print_tree(root)
