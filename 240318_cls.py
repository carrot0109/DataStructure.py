'''min, max'''
def find_min_max(A):
    min = A[0]
    max = A[0]
    
    for i in range(1, len(A)):
        if min > A[i]:
            min = A[i]
        if max < A[i]:
            max = A[i]
    
    return min, max     # 여러개의 값을 반환 가능함(튜플 형태)

data = [5, 8, 9, 6, 8, 6, 7, 3]
(x, y) = find_min_max(data)
print('max : %d, min : %d' %(x, y))


'''default argument'''
def sum_range(begin, end, step = 1):
    sum = 0

    for n in range(begin, end, step):
        sum += n
    
    return sum

if __name__ == "__main__":      # main function(The name is main, i.e. run a function when you call yourself)
    print('sum = %d' %sum_range(1, 10))
    print('sum = %d' %sum_range(1, 10, 2))
    print('sum = %d' %sum_range(step = 3, begin = 1, end = 10))


'''global scope'''
# don't using global variable
pi = 3.141592
perimeter = 0

def calc_perimeter(radius):
    global perimeter    # define same
    print('Pi :', pi)   # only reading is fine
    perimeter = 2 * pi * radius     # but '=' is not fine
    
if __name__ == "__main__":
    calc_perimeter(10)
    print(perimeter)


'''import module 1'''
import min_max      # bring min_max.py
import sum

# min_max --> Function is executed because it is not wrapped by the main function

data = [5,6,8,1,3,2,40]
print('min, max :', min_max.find_min_max(data))
print('sum :', sum.sum_range(1, 10))


'''import module 2'''
from min_max import find_min_max    # Ready to use find_min_max 
from sum import *   # '*' --> All identifiers available right away

data = [5,6,8,1,3,2,40]
print('min, max :', find_min_max(data))
print('sum :', sum_range(1, 10))


'''class car'''
class Car:
    # init : A constructor function that automatically invokes each time an object is created. Defining member variables
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def speedUp(self):
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

if __name__ == '__main__':
    car1 = Car('Black')    
    car2 = Car('Red', 100)
    car3 = Car('Yellow')
    # Think that all the colors and velocities are mapped onto a square, and that each variable points to it
    # so car1.color means color where car1 is pointing

    print('color : %s - speed : %d' %(car1.color, car1.speed))
    print('color : %s - speed : %d' %(car2.color, car2.speed))
    print('color : %s - speed : %d' %(car3.color, car3.speed))
