def printStep(L, idx):
    print("    Step %d : "%idx, end='')   
    print(L)

def selectionSort(L):
    n = len(L)      # 리스트의 길이

    for i in range(n-1):        # 마지막 숫자 전까지만 정렬 --> 마지막은 남은 숫자로 알아서 정렬
        least = i       # i 번째 기준
        for j in range(i + 1, n):       # i + 1 번째 이후부터 비교
            if L[j] < L[least]:     # 새로운 최솟값이 나왔을 때
                least = j

        L[i], L[least] = L[least], L[i]     # swap --> i 번째 숫자 정해짐
        # printStep(L, i + 1)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]      # 4 자리에 5 를 대입한다면 안전성을 보장하지 못함
    
    L = list(data)

    print("Before    : ", L)
    selectionSort(L)
    print("After     : ", L)
    print()