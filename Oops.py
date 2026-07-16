# in oops we use classes and objects and then save the details 
# it provides resuability and security
# classes = it is a blueprint for objects
# object is used to call the class
# varibles defined in class is attribute
class Factory:
    a = 12
    def hello(self):
        print("how are you")
    
    print("hello")
obj = Factory()
print(obj.a)
obj.hello()
# self is used for location transfer
# constructor = it runs automatically when we call class and this constructor function targets the location of object
class Factory1:
    def __init__(self,materials,pockets,zips):
        self.materials = materials
        self.zips = zips
        self.pockets = pockets
    def show(self):
        print(f"Your object details  are {self.materials} , {self.zips} , {self.pockets} ")
        
        
reebok = Factory1("Leather",3,2)

campus = Factory1("Nylon",4,5)
reebok.show()


# Types of attributes
class Animal:
    name = "Lion" # class attribute = declared inside the class
    def __init__(self, age): 
        self.age = age # instance attributes = declared as self
        
# Types of methods
    def show(self): # instance method = it will target objects
        pass
    @classmethod
    def hello(cls): # class method = it will target class
        pass
    @staticmethod
    def static():
        pass
obj = Animal()
obj.show()
obj.hello()
