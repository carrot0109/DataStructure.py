import queue

class TNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None        # root node

    def preOrder(self, node):
        if node is not None:
            print('[%c] ' %node.data, end='')       # V
            self.preOrder(node.left)        # L
            self.preOrder(node.right)       # R

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)     # L
            print('[%c] ' %node.data, end='')       # V
            self.inOrder(node.right)        # R

    def postOrder(self, node):
        if node is not None:
            self.postOrder(node.left)       # L
            self.postOrder(node.right)      # R
            print('[%c] ' %node.data, end='')       # V

    def levelOrder(self, node):
        Q = queue.Queue()
        Q.out(node)

        while not Q.empty():        # 비어있으면 멈춤
            node = Q.get()
            print('[%c] ' %node.data, end='')

            if node.left is not None:       # node 가 None 이면 X
                Q.put(node.left)
            if node.right is not None:
                Q.put(node.right)
            
    def nodeCount(self, node):
        count = 0
        if node != None:
            count = 1 + self.nodeCount(node.left) + self.nodeCount(node.right)
        return count
    
    def isExternal(self, node):
        return node.left == None and node.right == None     # 단말노드인지 확인
    
    def leafCount(self, node):
        count = 0
        if node != None:
            if self.isExternal(node):
                return 1        # 개수 추가
            else:
                count = self.leafCount(node.left) + self.leafCount(node.right)
        return count
    
    def getHeight(self, node):
        if node == None:
            return 0        # 0 을 할당함으로 선택되지 않음
        return max(self.getHeight(node.left), self.getHeight(node.right)) + 1       # 1 더해주는 것이 핵심


if __name__ == '__main__':
    T = BinaryTree()
    n6 = TNode('F')
    n5 = TNode('E')
    n4 = TNode('D')
    n3 = TNode('C', n6)
    n2 = TNode('B', n4, n5)
    n1 = TNode('A', n2, n3)

    print('Pre : ', end=''); T.preOrder(n1); print()
    print('In : ', end=''); T.inOrder(n1); print()
    print('Post : ', end=''); T.postOrder(n1); print()
    print('Level : ',end=''); T.levelOrder(n1); print()
    
    print('Node count : ', T.nodeCount(n1)); print()
    print('Leaf count : ', T.leafCount(n1)); print()
    print('Get Height : ', T.getHeight(n1)); print()