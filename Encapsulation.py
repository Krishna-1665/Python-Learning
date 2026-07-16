# it refers to data binding
# put code together and hide internal details and only shows what is needed

# Access modifier = giving access
# 1. Public = everyone can access
# 2. private = only can be accessed inside the same class inplementing using two underscore before variable
# 3. Protected = implement using underscore before variable

class Factory:
    _a = "pune" # protected
    __b = "Bihar" # private
    def show(self):
        print("hello i am a good factory")
        print(Factory.__b)
obj = Factory()
print(obj.a)
