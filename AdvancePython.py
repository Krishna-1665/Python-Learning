## Decorators
#  it modifies another fucntion without changing its actual code

def decorate(func):
    def wrapper(*args,**kwargs):
        print("Addition of your numbers are ")
        func(*args,**kwargs)
        print("Done ")
    return wrapper
@decorate
def addition(a,b):
    print(f"Your total is {a+b}")
addition(12,45)


## args(*) and kwargs(keyword args **) = keywords used in function to accept flexible number of arguments used in multiple items

def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i 
    print(sum)
addition(12,12,45)


def information(**kwargs):
    print("Your Indformation is \n\n")
    for i in kwargs:
        print(f"{i}:{kwargs[i]}")


information(name="Krishna",age=23,Designation="Full stack developer")

# comprehension  = it means everything writeen in one line
# list comprehension
l =[i for i in range(1,21) if i% 2==0]
print(l)

# dictionary
l = {i: i**2 for i in range(1,10) }
print(l)

# lambda Function

# it is anonymous function declared with lambda keyword
addition = lambda a,b: a+b
print(addition(23,45))

# Map and filter
# Map apply sthe same funtion to every item to a list
a = [1,2,3,4,5]

result =map( lambda x : x*2,a)
print(list(result))

# filter = used to filter something in a sequence

def even(x):
    if x%2==0:
        return True
    else:
        return False
    
a = [1,2,3,4,5,6,7,8,9]
result = filter(even , a)
print(list(result))
