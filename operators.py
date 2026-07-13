# 1. Arithemetic Operator 

# + = Addition  = Add numbers
# - = Substraction = Substract numbers
# * = Multiplication = = Multiply numbers
# / = Division = Divide Numbers
# // = Floor Division = Divide numbers but gives integer values
# ** = Exponential = to set power to any number
# % = Modulus = To take remainder

a=12
b=6

print(a+b)  
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(5**2)
print(a%b)
print(12+4/2)

# 2. Assignment Operator = Assihn the values
p=23
print(p)

#### Compound Assignment Operator = re-assigining the values 
a = 20
a+=20
a-=10
a*=10
a/=10
a**=10
a//=10
print(a)

# comparison Operator= compare between variables adn always boolean values

# for comparison we have
# <,>,<=,>=,==,!=

a = 13
b = 12
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(23>=23)

# unicode = ascii values
print(ord("A"))
print(ord("B"))
print("A">"B")
# same datatypes allowed only
print(a>34)


#  logical Operators
# it is used to combine multiple operations
# three types of logical operators 
# 1 and = return true if both conditions are true 
# 2 or = return true if any conditions are true
# 3 not = reverse the boolean values  


print(123>100 and 34==34 and 45>23)
print(123>100 and 34==34 or 45<23)
print( not 12==12)


