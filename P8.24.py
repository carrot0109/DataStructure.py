def isMinHeapRec(A, i):
    # 트리의 크기
    n = len(A)

    # 왼쪽 자식 인덱스
    left = 2 * i
    # 오른쪽 자식 인덱스
    right = 2 * i + 1

    # 현재 노드가 리프 노드인 경우, 최소 힙 조건을 만족함
    if left >= n:
        return True

    # 오른쪽 자식이 없고, 왼쪽 자식만 있는 경우
    if right >= n:
        # 현재 노드가 왼쪽 자식보다 작거나 같으면 최소 힙 조건을 만족함
        return A[i] <= A[left] and isMinHeapRec(A, left)

    # 현재 노드가 왼쪽 및 오른쪽 자식보다 작거나 같아야 함
    if A[i] <= A[left] and A[i] <= A[right]:
        # 왼쪽 및 오른쪽 서브트리도 최소 힙 조건을 만족해야 함
        return isMinHeapRec(A, left) and isMinHeapRec(A, right)

    return False

# Example usage:

# 최소 힙을 만족하는 배열
A = [0, 1, 2, 3, 4, 5, 6]

print(isMinHeapRec(A, 1))  # Output: True

# 최소 힙을 만족하지 않는 배열
B = [0, 1, 3, 2, 7, 6, 5]

print(isMinHeapRec(B, 1))  # Output: False
