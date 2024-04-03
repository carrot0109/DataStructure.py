class ArrayStack:

    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity -1
    
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.stack[self.top] = e
        else:
            print('Overflow!')

    def pop(self):
        if not self.isEmpty():
            e = self.stack[self.top]
            self.top -= 1
            return e
        else:
            print('Empty!')

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        else:
            print('Empty!')

    def sortedPush(self, e):
        if(self.isEmpty() or e > self.peek()):
            self.push(e)
        else:
            temp = self.pop()
            self.sortedPush(e)
            self.push(temp)

    def __str__(self):
        return str(self.stack[0 : self.top + 1])


if __name__ == '__main__':
    
    S = ArrayStack(10)
    data = [5, 3, 8, 1, 2, 7] 
    
    for d in data:
        S.sortedPush(d)
        print(S)

########################################################

from StackArray import ArrayStack

def chekBrackets(str):
    S = ArrayStack(100)

    for c in str:
        if c == '[' or c == '{' or c == '(':
            S.push(c)
        elif c == ']' or c == '}' or c == ')':
            if S.isEmpty():
                return False
            else:
                left = S.pop()
                if (c == ']' and left != '[') or (c == '}' and left != '{') or (c == ')' and left != '('):
                    return False
    
    return S.isEmpty()

if __name__ == '__main__':
    s1 = '{ A[(i + 1)] = 0 }'
    s2 = 'if((i == 0) && (j == 0)'
    s3 = 'A[(i + 1])'

    print(s1,'-->', chekBrackets(s1))
    print(s2,'-->', chekBrackets(s2))
    print(s3,'-->', chekBrackets(s3))

    
    filename = 'data_test.txt'
    infile = open(filename, 'r')
    str = infile.read()
    infile.close()

    print(filename, '-->', chekBrackets(str))

##################################################

from StackArray import ArrayStack

def evalPostfix(expr):
    S = ArrayStack()

    for token in expr:
        if token in '+-*/':
            val2 = S.pop()
            val1 = S.pop()
            if token == '+':
                S.push(val1 + val2)
            elif token == '-':
                S.push(val1 - val2)
            elif token == '*':
                S.push(val1 * val2)
            elif token == '/':
                S.push(val1 / val2)
        else:
            S.push(float(token))

    return S.pop()


if __name__ == '__main__':
    str = '8 2 / 3 - 3 2 * +'
    expr = str.split()      # delete space element
    print(str, '-->', evalPostfix(expr))

##################################################

from StackArray import ArrayStack

def precedence(op):
    if (op == '(' or op == ')'): return 0
    elif (op == '+' or op == '-'): return 1
    elif (op == '*' or op == '/'): return 2
    else: return -1

def infixToPostfix(expr):
    S = ArrayStack()
    postfix = []

    for term in expr:
        if term in '(':
            S.push(term)
        elif term in ')':
            while not S.isEmpty():
                op = S.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif term in '+-*/':
            while not S.isEmpty():
                op = S.peek()
                if(precedence(term) <= precedence(op)):
                    postfix.append(op)
                    S.pop()
                else: break
            S.push(term)
        else:
            postfix.append(term)

    while not S.isEmpty():
        postfix.append(S.pop())

    return postfix

if __name__ == '__main__':
    infix = input('Input infix expr : ')
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)

#####################################################

from EvalPostfix import evalPostfix
from InfixToPostfix import infixToPostfix

infix = input('Input infix expr : ')
expr = infix.split()

print(expr, '=', evalPostfix(infixToPostfix(expr)))
