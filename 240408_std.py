from ArrayStack import ArrayStack

map = [
    ['1', '1', '1', '1', '1', '1'],
    ['e', '0', '0', '0', '0', '1'],
    ['1', '0', '1', '0', '1', '1'],
    ['1', '1', '1', '0', '0', 'x'],
    ['1', '1', '1', '0', '1', '1'],
    ['1', '1', '1', '1', '1', '1']
]

SIZE = 6

def isValidPos(r, c):   # r : row, c : column
    if  0 <= r < SIZE and 0 <= c < SIZE:
        if map[r][c] == '0' or map[r][c] == 'x':
            return True
    return False

def DFS():
    print('DFS : ')
    S = ArrayStack()

    S.push((1, 0))
    while not S.isEmpty():
        pos = S.pop()
        print(pos, end=' -> ')
        (r, c) = pos
        if map[r][c] == 'x':
            return True
        
        else:
            map[r][c] = '.'
            if isValidPos(r - 1, c):
                S.push((r - 1, c))
            if isValidPos(r + 1, c):
                S.push((r + 1, c))
            if isValidPos(r, c - 1):
                S.push((r, c - 1))
            if isValidPos(r, c + 1):
                S.push((r, c + 1))
        
        S.display()

    return False


if __name__ == '__main__':
    res = DFS()

    if res:
        print('SUCCESS')
    else:
        print('FAILURE')
