from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def find_node_level(root, target):
    if not root:        # 루트가 None 이라면 0 반환
        return 0
    
    queue = deque([(root, 1)])  # (node, level) 초기화

    while queue:
        node, level = queue.popleft()
        
        if node.value == target:
            return level
        
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    
    return 0

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

# Finding levels of different nodes
print(find_node_level(root, 1))  # Output: 1
print(find_node_level(root, 2))  # Output: 2
print(find_node_level(root, 4))  # Output: 3
print(find_node_level(root, 6))  # Output: 3
print(find_node_level(root, 7))  # Output: 0 (node not in the tree)
