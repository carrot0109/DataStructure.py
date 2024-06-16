N = 100

class MaxHeap:      # 최대 힙 기준
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def insertItem(self, e):
        self.heapSize += 1      # 한 칸을 늘린다고 생각
        self.heap[self.heapSize] = e        # 늘린 칸에 삽입

        self.upHeap()       # 순서 정렬

    def upHeap(self):
        i = self.heapSize
        item = self.heap[i]

        while i != 1 and item > self.heap[i // 2]:      # 부모보다 크다면
            self.heap[i] = self.heap[i // 2]        # 부모를 끌어내림
            i = i // 2      # 자기가 부모가 됨

        self.heap[i] = item     # 최종적으로 부모에다 맨 마지막 말단 저장

    def removeItem(self):
        e = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]     # 루트에다 말단 삽입
        self.heapSize -= 1      # 말단 제거

        self.downHeap()
        return e
    
    def downHeap(self):
        e = self.heap[1]        # 현재 루트 / 전직 말단
        p = 1       # 부모
        c = 2       # 자식

        while c <= self.heapSize:       # 루트를 계속 끌어내릴건데, 가장 말단보다 아래로는 못내려간다
            if c < self.heapSize and self.heap[c + 1] > self.heap[c]:       # 형제가 더 크다면 큰 쪽으로 / 등호가 없는 이유 : 말단일 때 (완전 이진 트리이기에 말단일 때만 형제가 존재하지 않을 수 있다)
                c += 1

            if e >= self.heap[c]:       # 부모가 자식보다 크거나 같다면 최대힙 만족 --> break
                break

            self.heap[p] = self.heap[c]     # 형제 중 더 큰 자식을 부모로 끌어올림
            p = c       # 부모 위치 재정의
            c *= 2      # 부모의 왼쪽 자식으로 재정의

        self.heap[p] = e        # 최종적으로 선정된 부모 자리에 말단 삽입
            

if __name__ == '__main__':
    H = MaxHeap()
    data = [7, 3, 5, 6, 4, 9, 2, 3, 1, 2]

    for e in data:
        H.insertItem(e)
        print('Heap :', H.heap[1:H.heapSize + 1])
    print()

    print('[%d] is deleted' %H.removeItem())
    print('Heap :', H.heap[1:H.heapSize + 1])
    print('[%d] is deleted' %H.removeItem())
    print('Heap :', H.heap[1:H.heapSize + 1])