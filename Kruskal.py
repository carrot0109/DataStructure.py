# 그래프 정의: 각 정점과 연결된 정점 및 가중치를 나타냄
Graph = {
    'A': [('B', 29), ('F', 10)],
    'B': [('A', 29), ('C', 16), ('G', 15)],
    'C': [('B', 16), ('D', 12)],
    'D': [('C', 12), ('E', 22), ('G', 18)],
    'E': [('D', 22), ('F', 27), ('G', 25)],
    'F': [('A', 10), ('E', 27)],
    'G': [('B', 15), ('D', 18), ('E', 25)]
}

# 정점의 부모를 저장하는 리스트: 초기에는 모든 정점이 자기 자신이 루트임
vertices = [-1, -1, -1, -1, -1, -1, -1]

# 모든 엣지를 저장할 리스트
eList = []

# 엣지를 추출하고 가중치에 따라 정렬하는 함수
def edgeSort():
    # 그래프에서 모든 엣지를 추출
    for v in Graph:
        for e in Graph[v]:
            # 엣지를 중복으로 추가하지 않기 위해 v < e[0]인 경우만 추가
            if v < e[0]:
                eList.append([v, e[0], e[1]])

    # 엣지를 가중치에 따라 내림차순으로 정렬
    eList.sort(key=lambda e: e[2], reverse=True)

    # 정렬된 엣지를 역순으로 출력 (가중치가 작은 순으로)
    for i in range(len(eList) - 1, -1, -1):
        print('[%c%c%d] ' % (eList[i][0], eList[i][1], eList[i][2]), end='')
    print()
    print()

# 정점이 속한 집합의 루트를 찾는 함수
def find(vNum):
    # 루트를 찾을 때까지 부모를 따라감
    while vertices[vNum] != -1:
        vNum = vertices[vNum]
    return vNum

# 두 집합을 합치는 함수
def union(vNum1, vNum2):
    # vNum1을 vNum2의 부모로 설정
    vertices[vNum2] = vNum1

# 크루스칼 알고리즘을 사용하여 MST를 찾는 함수
def kruskal():
    # MST에 포함된 엣지의 수
    eCnt = 0
    # 그래프의 정점 수
    vCnt = len(Graph)
    # 엣지를 추출하고 정렬
    edgeSort()

    # MST의 엣지 수가 정점 수 - 1이 될 때까지 반복
    while eCnt < vCnt - 1:
        # 가장 작은 엣지를 팝
        e = eList.pop()
        # 엣지의 두 정점이 속한 집합의 루트를 찾음
        vNum1 = find(ord(e[0]) - 65)
        vNum2 = find(ord(e[1]) - 65)

        # 두 정점이 다른 집합에 속한 경우
        if vNum1 != vNum2:
            # MST에 엣지를 추가하고 엣지 수를 증가
            eCnt += 1
            print('%d. [%s%s %d]' % (eCnt, e[0], e[1], e[2]))
            # 두 집합을 합침
            union(vNum1, vNum2)

# 메인 함수: 스크립트가 실행될 때 크루스칼 알고리즘을 수행
if __name__ == '__main__':
    kruskal()
