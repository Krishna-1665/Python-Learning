# it uses hash value to store values
# mutable
# unordered
# no duplicates
# hetrogeneous
s = {1,2,3,4,8,5,6.7,"krishna"}
for i in s:
    print(i)
a=hash("hello")
print(a)


# set methods
# remove = remove specific elements
# clear = remove all elements
# pop = remove less hash valuue number
# add = add a element
# | pipe for uniion
# & is used for intersection
# operation on multiple sets
# - for difference
# ^ for symmetric difference
b = {1,2,3,4,5,5,6,6,6,67}
c = {3,4,5,6,7,8,9}
s=b|c 
s=b&c
c-=b
s=b^c
print(s)