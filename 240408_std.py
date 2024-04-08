from ArrayStack import ArrayStack
MAZE_SIZE = 6

def isValidPos(x,y):
    if 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE:       # is inner of maze? and can I go there?
        if map[y][x] == '0' or map[y][x] == 'x':
            return True
    return False

def DFS():
    print('DFS : ')
    stack = ArrayStack(100)
    stack.push((0,1))       # start point

    while not stack.isEmpty():
        here = stack.pop()
        print(here, end=' ->')
        (x,y) = here

        if(map[y][x] == 'x'):       # x --> end point
            return True
        else:
            map[y][x] = '.'     # visited
            if isValidPos(x, y - 1): stack.push((x, y - 1))   # up
            if isValidPos(x, y + 1): stack.push((x, y + 1))   # down
            if isValidPos(x - 1, y): stack.push((x - 1, y))   # left
            if isValidPos(x + 1, y): stack.push((x + 1, y))   # right
        print(' 현재 스택:', stack)

    return False        # Failure of search


if __name__ == '__main__':
    map = [
        ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '1', '1', '0', '0', 'x'],
        ['1', '1', '1', '0', '1', '1'],
        ['1', '1', '1', '1', '1', '1']
    ]

    result = DFS()
    if result : print(' --> 미로 탐색 성공')
    else : print(' --> 미로 탐색 실패')
