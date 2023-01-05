# Collins Wanga

class Circle:
    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius * radius * Circle.pi
    def setRadius(self, newRadius):
        self.radius = newRadius
        self.area = newRadius * newRadius * self.pi
    def getCircumference(self):
        return self.radius * self.pi * 2
