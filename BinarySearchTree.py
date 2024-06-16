class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root == None:        # 탐색 성공
        return TreeNode(key)        # 노드 생성
    
    if key < root.key:      # 더 작음
        root.left = insert(root.left, key)      # 더 작으니까 왼쪽 노드 기준으로 다시 시작

    elif key > root.key:        # 더 큼
        root.right = insert(root.right, key)        # 더 크니까 오른쪽 노드 기준으로 다시 시작

    return root     # 중복 배제

def inOrder(root):      # 중위
    if root:
        inOrder(root.left)
        print('%2d ' %root.key, end='')
        inOrder(root.right)

def display(root, msg):
    print(msg, end='')
    inOrder(root)
    print()

def delete(root, key):
    if root == None:        # 공백 트리
        return None
    
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left == None:       # 왼쪽 자식 노드가 없는 경우
            return root.right       # 나머지 노드 끌어올림 / None 가능
        elif root.right == None:        # 왼쪽 노드는 존재하지만 오른쪽 노드 없는 경우
            return root.left        # 남아있는 왼쪽 노드 끌어올림
        else:       # 자식 노드 2개 모두 있을 때
            succ = getMinNode(root.right)       # 후계자를 찾음
            root.key = succ.key     # 후계자의 키 복사
            root.right = delete(root.right, succ.key)       # 후계자 제거
        
    return root     # 탐색 실패

def getMinNode(root):       
    while root != None and root.left != None:
        root = root.left

    return root


if __name__ == '__main__':
    root = None
    data = [35, 18, 7, 26, 3, 22, 30, 12, 26, 68, 99]

    for key in data:
        root = insert(root, key)
        display(root, '[Insert %2d] : ' %key)

    # root = delete(root, 30)
    # display(root, '[Delete 30] : ')
    # root = delete(root, 26)
    # display(root, '[Delete 26] : ')

    root = delete(root, 35)
    display(root, '[Delete 35] : ')