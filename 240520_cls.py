import random
from SelectionSort import selectionSort

def rBinarySearch(A, key, low, high):
    if low > high:      # low 가 high 보다 큰 값을 가진다는 것은 범위가 잘못되었다는 것을 의미 --> 찾는 값이 없음을 의미
        return -1
    
    mid = (low + high) // 2     # 중앙값
    # 보간 --> mid = int(low + (high - low) * (key - A[low]) / (A[high] - A[low]))
    print(A[mid], end=' ')

    if key == A[mid]:       # 중앙값이 찾는 값이라면
        return mid
    elif key < A[mid]:      # 찾는 값이 중앙값 왼쪽에 위치한다면
        return rBinarySearch(A, key, low, mid - 1)      # 중앙값 기준 왼쪽을 관찰해야하기 때문에 high = mid - 1
    else:       # 중앙값 오른쪽에 위치한다면
        return rBinarySearch(A, key, mid + 1, high)     # 중앙값 기준 오른쪽을 관찰해야하기 때문에 low = mid + 1
    
def iBinarySearch(A, key):
    low = 0
    high = len(A) - 1

    while(low <= high):     # 첫번째 수와 마지막 수까지 비교
        mid = (low + high) // 2
        # 보간 탐색 --> mid = int(low + (high - low) * (key - A[low]) / (A[high] - A[low]))
        print(A[mid], end=' ')
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1


if __name__ == '__main__':
    A = []
    for i in range(15):
        A.append(random.randint(1, 100))        # 임의의 값 배정
    
    selectionSort(A)        # 순차적으로 정렬
    print('A[] =', A)

    key = int(input('input search key : '))
    print('rBinarySearch : %d\n' %rBinarySearch(A, key, 0, 14))
    
    key = int(input('input search key : '))
    print('iBinarySearch : %d' %iBinarySearch(A, key))
