with open("harry2.txt") as f:
    a=f.read()
    print(a)


f=open("harry2.txt","rt")
#print(f.readlines())
print(f.readline())
print(f.readline())

f.close()