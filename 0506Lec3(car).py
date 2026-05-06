class Car:

    def __init__(self, name="", speed=0):
        self.name=name
        self.speed=speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def speedUp(self, value=0):
        self.speed += value

    def speedDown(self, value=0):
        self.speed -= value

    def __str__(self):
        return '{}의 속도는 {}입니다.'.format(self.name, self.speed)

class Sedan(Car):
    def speedUp(self, value):
        self.speed += value
        if self.speed > 150:
            self.speed = 150

    def speedDown(self, value):
        self.speed -= value
        if self.speed < 0:
            self.speed = 0
            
myCar = Sedan("K5", 50)
myCar.speedDown(100)
print(myCar)

