N = 100

class MaxHeap:      # 최대 힙 기준
    def __init__(self):
        self.heap = [None] * N
        self.heapSize = 0

    def insertItem(self, e):
        self.heapSize += 1
        self.heap[self.heapSize] = e

        self.upHeap()

    def upHeap(self):
        i = self.heapSize
        item = self.heap[i]

        while i != 1 and item > self.heap[i // 2]:
            self.heap[i] = self.heap[i // 2]
            i = i // 2

        self.heap[i] = item

    def removeItem(self):
        e = self.heap[1]
        self.heap[1] = self.heap[self.heapSize]
        self.heapSize -= 1

        self.downHeap()
        return e
    
    def downHeap(self):
        e = self.heap[1]
        p = 1
        c = 2

        while c <= self.heapSize:
            if c < self.heapSize and self.heap[c + 1] > self.heap[c]:
                c += 1

            if e >= self.heap[c]:
                break

            self.heap[p] = self.heap[c]
            p = c
            c *= 2

        self.heap[p] = e
            

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
