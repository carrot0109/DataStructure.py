def printStep(L, idx):
    print("    Step %d : "%idx, end='')
    print(L)

def bubbleSort(L):
    n = len(L)
    for i in range(n - 1, 0, -1):       # i --> i 번 비교, 교환 / n - 1 부터인 이유는 맨 마지막은 그 뒤 인자가 없기 때문에 그 앞까지만 기준이 됨
        bChanged = False        # 교환이 이루어졌는지 확인 --> 한번도 교환이 이루어지지 않았다면 리스트는 정렬이 완벽한 상태
        for j in range(i):      # 처음부터 i 번 비교, 교환
            if L[j] > L[j + 1]:     # j 번째 숫자가 더 크다면 교환
                L[j], L[j + 1] = L[j + 1], L[j]     # swap
                bChanged = True     # 교환이 이루어짐 --> True
                
        if not bChanged: break      # 한 번도 교환이 이루어지지 않음 --> 완벽한 정렬 상태
        printStep(L, n - i)

if __name__ == "__main__": 
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]   
    
    L = list(data)

    print("Before     :", L)
    bubbleSort(L)
    print("After      :", L)
    print()