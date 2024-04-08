class circularQueue:

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else:
            pass

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else:
            pass

    def peek(self):
        if not self.isEmpty():
            return self.queue[(self.front + 1) % self.capacity]
        else:
            pass

    def display(self):
        print('Front : %d, Rear : %d' %(self.front, self.rear))
        i = self.front

        while i != self.rear:
            i = (i + 1) % self.capacity
            print('[%c] ' %self.queue[i], end='')


if __name__ == '__main__':
    Q = circularQueue()
    Q.enqueue('A')
    Q.enqueue('D')
    Q.enqueue('E')
    Q.enqueue('C')
    Q.enqueue('B')
    Q.display()
    print()

    print('Dequeue -->', Q.dequeue())
    print('Dequeue -->', Q.dequeue())
    print('Dequeue -->', Q.dequeue())
    Q.display()
    print()

    print('Peek -->',Q.peek())
    Q.display()
    print()

    Q.enqueue('G')
    Q.enqueue('T')
    Q.enqueue('M')
    Q.enqueue('P')
    Q.display()
    print()
