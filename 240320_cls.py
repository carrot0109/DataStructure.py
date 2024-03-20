'''Car module'''
class Car:
    # init : A constructor function that automatically invokes each time an object is created. Defining member variables
    def __init__(self, color, speed = 0):
        self.color = color
        self.speed = speed

    def speedUp(self):      # method(self) : Object-only function
        self.speed += 10

    def speedDown(self):
        self.speed -= 10

    def isEqual(self, oCar):
        if self.color == oCar.color: 
            return True
        else: 
            return False

    def __eq__(self, oCar):     # Return string type
        return 'YES' if self.color == oCar.color else 'NO'

    def __str__(self):          # Return string type
        return 'color = %s, speed = %d' %(self.color, self.speed)
    
    def __ge__(self, oCar):
        return "Faster" if self.speed >= oCar.speed else "Slower"


if __name__ == '__main__':
    car1 = Car('Black', 0)    
    car2 = Car('Red', 100)
    car3 = Car('Yellow')
    # Think that all the colors and velocities are mapped onto a square, and that each variable points to it
    # so car1.color means color where car1 is pointing

    # print('color : %s - speed : %d' %(car1.color, car1.speed))
    # print('color : %s - speed : %d' %(car2.color, car2.speed))
    # print('color : %s - speed : %d' %(car3.color, car3.speed))

    # car1.speedUp()
    # car2.speedDown()

    # print('color : %s - speed : %d' %(car1.color, car1.speed))
    # print('color : %s - speed : %d' %(car2.color, car2.speed))
    # print('color : %s - speed : %d\n' %(car3.color, car3.speed))

    print(car1.isEqual(car2))
    print(car1 == car2)

    print('[car3]',car3)

    print(car1 >= car2)



'''superCar module'''
from Car import Car

class SuperCar(Car):
    def __init__(self, color, speed = 0, bTurbo = True):
        # self.color = color
        # self.speed = speed
        super().__init__(color, speed)       # super() : Call the parent's creator directly
        self.bTurbo = bTurbo

    def setTurbo(self, bTurbo = True):       # Method of turning on or turning off bTurbo
        self.bTurbo = bTurbo

    def speedUp(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speedUp()       # Function defined on parent's (self.speed += 10)

    def __str__(self):
        if self.bTurbo:
            return '[%s][speed = %d] Turbo' %(self.color, self.speed)
        else:
            return '[%s][speed = %d] Normal' %(self.color, self.speed)


if __name__ == '__main__':
    s1 = SuperCar("Gold")
    s2 = SuperCar("Silver", 50, False)

    print(s1)
    print(s2)
    print()

    s1.speedUp()
    s2.speedUp()
    print(s1)
    print(s2)
