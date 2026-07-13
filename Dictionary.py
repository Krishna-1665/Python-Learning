# it is used to store pair of keys and values
# in other programming language it is called hash map

# empty set is a dictionary

# it is  mutable(keys cannot be changes but values can be)
# keys are unique and values can be common
# it follows insertion order
# it is hetrogeneous
# it can be accessed by using keys 

d = {1:"hello"}
d[1] = "krishna" #updating
d[50] = "python" # creating
del d[50] # deleting
print(type(d))
print(d[1])

a = [10,20,30]
print(a[0])

# dictionary traversing
# methods:- clear,copy ,pop = remove only key,pop-items = remove a pair , update
d = {10:100,20:200,30:300}
for i in d:
    print(i)
    print(d[i])
# deep copy = assigned value will also change the main value
m = [1,2,3,4,5]
b= m
b[0] = 100
print(b)

# shalow copy uses .copy function  = assigned value will not change the main value
m = [1,2,3,4,5]
b = m.copy()
b[0] = 100
print(b)
