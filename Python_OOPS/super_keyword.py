class Rectangle:
    def __init__(self,length,width,height):
        self.length=length
        self.width=width
        self.height=height

class Square(Rectangle):
    def __init__(self,length,width,height=None):
        super().__init__(length,width,height)
    def area(self):
        return self.length * self.width
    
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width,height)

    def volume(self):
        return self.length *self.width * self.height

square = Square(3,3)
cube = Cube(3,3,3)
print(square.area())
print(cube.volume())

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

P=Person("Guna",19)
print(P.name, P.age)    
