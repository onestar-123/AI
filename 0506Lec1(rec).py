class Rectangle:
    def __init__(self, side=0):
        self.side =side

    def getArea(self):
        return self.side*self.side
    
r1 = Rectangle(10.0)
