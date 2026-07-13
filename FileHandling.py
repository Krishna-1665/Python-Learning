# file handling refers to reading,creating,Deleting and writing the file(CRUD)
# always close the file after opening
# 'r'  = readmode
# 'a' = appendmode = add new content to the file without anything in the file
# 'w' = writemode = create or override(remove past content and then add new content)
# 'x' = createmode

p=open(r"List.py")
print(p.read())
r=open("superman.txt","w")
r.write("Python learning")
r.close()

