# # In this a child class take the properties of parent class
# # child class = it Inherits the parent class also called as subclass
# # parent class = Inherited by child class also called as superclass
# # it provides us code resuability

class Factory: # parent class
    def hello(self):
        print("I am a method")
class Factory2(Factory): # child class
    pass
obj = Factory2()
print(obj.hello())


# # constructor in inheritance
# # super function targetes super class/ parent class
class Animal:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"Hello your name is {self.name} and age is {self.age}")
class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
        
        
person1 = Human("Krishna",23)
person1.show()


# # Types of Inheritance
# # 1. single Inheritance = one parent and one child class
# # 2. Multiple Inheritance = multiple parent and one child class


# # Multiple Inheritance
class Animal:
    name1 = "lion"
class Human:
    name2 = "Harsh"
class Robots(Animal,Human):
    name3 = "Charlie"
obj = Robots()
print(obj.name1)
print(obj.name2)
print(obj.name3)

# 3 . Multilevel Inheritance = level wise Inheritance

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class Machine(Factory):
    def __init__(self,material,zips,color):
        super().__init__(material,zips)
        self.color = color
class Products(Machine):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets

