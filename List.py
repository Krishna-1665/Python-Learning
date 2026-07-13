
# it is stored in square video
#  mutable = chageble
#  duplicates value
#  ordered = maintain the sequence
#  hetrogenious = multiple datatypes can be stored in this
 
a = [12,13,14,15,16,11,11,11,"Krishna"]
print(a[0:5])

 # list traversing and methods = using loops in list

a=[12,13,14,15]
for i in range(len(a)):
    print(a[i])

# methods() = defined in class
# append = add new values at end
# count = counts number of occurence of  values
# extend = add multiple items at the last
# remove = remove any values of first occurence
#  insert  = add on index number privided by user(index number,what to insert)

l=[1,3,4,5]
l.append(6)
l.insert(1,2)
l.remove(2)
l[0] = 10
print(l[0])
print(l)

z = [-45,67,12,-68,34]
print("Positive elements are ")
for i in z:
    if i >= 0:
        print(i)
print("Negative elements are ")
        
for i in z:
    if i<0:
        print(i)
        
        