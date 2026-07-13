# error occur during runtime
# nothing will be execute after exception

a = int(input("enter your number"))
try:
    
    print(10/a)
except Exception as err:
    print("you cannot divide by 0")
else:
    print("Good there is no exception")   
    
finally:
    print("I will run always")

print("Division done")

# keywords
# try = wrap the code that might cause Exception
# except = handle the Exception if it occurs
# else = it runs when except doesnot run
# finally  = it will run always
# raise = manually throw an exception 

age = int(input("tell me your age"))
if age < 10 or age > 18:
    raise ValueError("sorry you are no eligible")
else:
    print("you are eligible")
print("the club will start soon ")
