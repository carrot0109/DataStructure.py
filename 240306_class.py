'''팩토리얼(반복문)'''
def iFact(n):
    res = 1
    for i in range(n, 0, -1):
        res *= i
    return res

'''팩토리얼(재귀문)'''
def rFact(n):
    if n == 1:
        return 1
    else:
        return n * rFact(n - 1)
    
print('rFact : %d, iFact : %d' % (rFact(5), iFact(5)))
