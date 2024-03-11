'''거듭제곱(반복문)'''
def iPower(x, n):
    result = 1
    for i in range(n):
        result *= x

    return result

'''거듭제곱(순환문)'''
# n이 극도로 커질수록 효율적임(로그 2의 n 시간복잡도)
def rPower(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return rPower(x*x, n//2)
    else:
        return x * rPower(x*x, (n-1)//2)

print("iPower : %d" %(iPower(2, 10))) 
print("rPower : %d" %(rPower(2, 10)))


'''피보나치(순환문)'''
count = 0

def rFib(n):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rFib(n-2) + rFib(n-1)
    
print("rFib : %d, count : %d" %(rFib(10), count))

'''피보나치(반복문)'''
def iFib(n):
    if n < 2:
        return n
    
    pp = 0
    p = 1
    for i in range(2,n + 1):
        current = p + pp
        pp = p  # n-2 --> n-1
        p = current
        
    return current

print('iFib : %d'%(iFib(10)))


'''하노이탑(순환)'''
def hanoiTower(n, fr, tmp, to):
    if n == 1:
        print('Disk %d : %s -- > %s'%(n, fr, to))
    else:
        hanoiTower(n-1, fr, to ,tmp)
        print('Disk %d : %s -- > %s'%(n, fr, to))
        hanoiTower(n-1, tmp, fr, to)

hanoiTower(3, 'A', 'B', 'C')
