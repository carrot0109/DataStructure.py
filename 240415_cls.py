from CircularQueue import circularQueue

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '1', '0', '0', '1'],
    ['1', '0', '0', '0', '1', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '0', '1', '0', '0', 'x'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):
    if  0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False

def BFS():
    Q = circularQueue(100)

    Q.enqueue((1,0))
    print('BFS : ')
    
    while not Q.isEmpty():
        pos = Q.dequeue()
        print(pos, end=' -> ')

        (r, c) = pos
        if map[r][c] == 'x':
            return True
        
        else:
            map[r][c] = '.'
            if isValidPos(r - 1, c):
                Q.enqueue((r - 1, c))
            if isValidPos(r + 1, c):
                Q.enqueue((r + 1, c))
            if isValidPos(r, c - 1):
                Q.enqueue((r, c - 1))
            if isValidPos(r, c + 1):
                Q.enqueue((r, c + 1))
        
        Q.display2()

    return False


if __name__ == '__main__':
    res = BFS()

    if res:
        print('SUCCESS')
    else:
        print('FAILURE')
