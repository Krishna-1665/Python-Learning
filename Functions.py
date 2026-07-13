# it is resuable block of code that can be executed whenever we want to call it

def hello():
    print("this is a hello function")

hello()

# Paramerters and Arguments
# Parameters are variables declared inside functions while defining the function
# Arguments are variables declared inside functions while calling the function

# Types of arguments

# 1 Positional arguments

def sum(a,b): 
    print(f"sum of your numbers is {a+b}")
sum(10,20)
sum(45,67)

# 2 Keyword arguments
def hello(name,age):
    print(f"your name is {name} and age is {age}")
hello(age=23,name="Krishna")

# 3 Default Arguments
def sum(a,b=45): 
    print(f"sum of your numbers is {a+b}")
sum(10)

def palindrome(st):
    rev=""
    for i in range (len(st)-1,-1,-1):
        rev = rev+st[i]
    
    if rev == st:
        print("It is palindrome")
    else:
        print("It is not palindrome")
palindrome("naman")
palindrome("cursor")    

    
# Return - it return the value where it is called
def hello():
    return("lets go")
print(hello())