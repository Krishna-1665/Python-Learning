# poly means many and morphism means form
# same name having different forms
# two ways to acheive polymorphism
# 1. Method overriding
class Animal:
    def show(self):
        print("Hello i am lion")  
class Human(Animal):
    def show(self):
        print("Hello i am Krishna")
obj = Human()
obj.show()       

# 2. Duck typing
class Parent:
    def care(self):
        print("i am loving")
class child:
    def care(self):
        print("i am geting loved")
obj = Parent()
obj2 = child()
obj.care()
obj2.care()

