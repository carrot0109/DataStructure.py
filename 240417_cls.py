from CircularQueue import *

class CircularDeque(CircularQueue):

    def __init__(self, capacity = 10):
        super().__init__(capacity)
    
    def addFront(self, e):
        if not self.isFull():
            self.array[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else:
            pass

    def deleteFront(self):
        super().dequeue()
    
    def getFront(self):
        super().peek()

    def addRear(self, e):
        super().enqueue(e)

    def deleteRear(self):
        if not self.isEmpty():
            e = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return e
        else:
            pass

    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        
if __name__ == '__main__':
    import random
    dq = CircularDeque()
    for i in range(4):
        dq.addFront(random.randint(65, 90))
    dq.display()

#################################################################################

import queue

Q = queue.Queue(maxsize=20)

for v in range(1, 10):
    Q.put(v)

print('Queue : ', end='')

for _ in range(1,10):
    print(Q.get(), end=" ")
print()


S = queue.LifoQueue(maxsize=20)

for v in range(1, 10):
    S.put(v)

print('Stack : ', end='')

for _ in range(1,10):
    print(S.get(), end=" ")
print()
