from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_complete_binary_tree(root):
    if not root:
        return True

    queue = deque([root])
    reached_end = False

    while queue:
        node = queue.popleft()

        if node:
            if reached_end:     # None 에 도달했었을 때만 실행 --> 그럼에도 node 가 존재한다는 것은 완전이진트리가 아니라는 것을 의미
                return False

            queue.append(node.left)
            queue.append(node.right)
        else:
            reached_end = True

    return True

# Example usage:
# Constructing a complete binary tree
#         1
#        / \
#       2   3
#      / \ /
#     4  5 6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(is_complete_binary_tree(root))  # Output: True

# Constructing a non-complete binary tree
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

print(is_complete_binary_tree(root))  # Output: False
