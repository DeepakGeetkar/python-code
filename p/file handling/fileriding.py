# f=open("deepak.txt")
# content=f.read()
# print(content)

# f.close()

###########################

f=open("deepak.txt","rt")
# content=f.read()
# print(content)
# print(f.readline())
# print(f.readline())
# print(f.readline())
##$###print(f.readlines())
for line in f:
    print(line,end=" ")

f.close()
