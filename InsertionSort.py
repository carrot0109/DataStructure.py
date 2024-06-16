def printStep(L, idx):
    print("    Step %d : "%idx, end='')
    print(L)

def insertionSort(L):
    n = len(L)
    for i in range(1, n):       # 첫 번째 패는 이미 정렬됨 --> 두 번째 자리부터는 새로 인자를 받아서 정렬
        key = L[i]      # 비교할 기준점
        j = i - 1       # 기준점 전 요소와 비교
        while j >= 0 and key < L[j]:        # 기준점이 더 작은 동안 반복
            L[j + 1] = L[j]     # 기준보다 더 큰 요소들은 한 칸씩 이동
            j -= 1      # 다음 요소로 이동
        L[j + 1] = key      # 기준점이 더 크다면 그 다음 자리에 기준점 삽입
        printStep(L, i)

    
if __name__ == "__main__": 
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]   
    
    L = list(data)

    print("Before    : ", L)
    insertionSort(L)
    print("Selection : ", L)
    print()