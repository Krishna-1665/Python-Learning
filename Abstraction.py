# refets to data hiding hide internal details and only shows what is needed
# if want to set up some rules we use absraction

from abc import ABC,abstractmethod

class Abstract(ABC): # abstract class
    @abstractmethod # Decorators
    def perimeter(self):
        pass
    
    @abstractmethod
    def area(self):
        pass
    
    
class Square(Abstract):
    def __init__(self,side):
        self.side = side
class Circle(Abstract):
    def __init__(self,radius):
        self.radius = radius
    def perimeter(self):
        print("I have created")
    def area(self):
        print("I have created a game")    
obj = Circle(3)




