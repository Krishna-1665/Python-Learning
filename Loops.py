# it allows us  execute a block of code multiple times without writing the same code
# two types
# 1 . For loops  = when we know the ending of loops 

for i in range(1,21,1):
    print(i)

for a in range(16,0,-1):
    print(a)
    
for a in range(-5,16,-1):
    print(a)
    
# #  Print table   
n= int(input("Enter the number"))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
    
    
a="KRISHNA"
# finding length and print number letter one by one
print(len(a))
for i in range(7):
    print(a[i])
for i in range(len(a)):
    print(a[i])

a="KRISHNA IS GOOD"
for i in a:
    print(i)
    
# break and continue
# Break  = to get stop
# else = if break doesnot execute the else will do

for i in range(1,21):
    if i == 15:
        break
    else:
        print(i)

# continue = to skip the part
for i in range(1,21):
    if i == 15:
        continue
    print(i)

# it repeats the code as long as condition is true

a = 1

while a <=30:
    print(a)
    a = a+1
    
a = int(input("enter the number"))
copy = a
rev = 0
while a>0:
    rev = rev*10 +a%10
    a= a//10
print(rev)
if copy == rev:
    print("Palindromic Number")
else: 
    print("Not a Palindromic Number")


