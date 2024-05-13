def printStep(L, idx):
    print("    Step %d : "%idx, end='')
    print(L)

def selectionSort(L):
    n = len(L)

    for i in range(n-1):
        least = i
        for j in range(i + 1, n):
            if L[j] < L[least]:
                least = j

        L[i], L[least] = L[least], L[i]
        printStep(L, i + 1)

if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]      # 4 자리에 5 를 대입한다면 안전성을 보장하지 못함
    
    L = list(data)

    print("Before    : ", L)
    selectionSort(L)
    print("Selection : ", L)
    print()

#################################

def printStep(L, idx):
    print("    Step %d : "%idx, end='')
    print(L)

def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        key = L[i]
        j = i - 1
        while j >= 0 and key < L[j]:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = key
        printStep(L, i)

    
if __name__ == "__main__":
    data = [5, 3, 8, 4, 9, 1, 6, 2, 7]      # 4 자리에 5 를 대입한다면 안전성을 보장하지 못함
    
    L = list(data)

    print("Before    : ", L)
    insertionSort(L)
    print("Selection : ", L)
    print()
