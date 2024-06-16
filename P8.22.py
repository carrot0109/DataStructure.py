class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sum_of_path_lengths(root):
    def dfs(node, depth):
        if not node:
            return 0
        
        # 현재 깊이 더하기 왼쪽과 오른쪽 서브트리의 깊이 합
        return depth + dfs(node.left, depth + 1) + dfs(node.right, depth + 1)       # depth 를 적절하게 활용하는 것이 중요
    
    return dfs(root, 0)

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

print(sum_of_path_lengths(root))  # Output: 8

# Explanation:
# Depth of node 1 (root) = 0
# Depth of node 2 = 1
# Depth of node 3 = 1
# Depth of node 4 = 2
# Depth of node 5 = 2
# Depth of node 6 = 2
# Total path length sum = 0 + 1 + 1 + 2 + 2 + 2 = 8
