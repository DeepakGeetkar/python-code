num=int(input("enter your number"))
first=0
second=1
for i in range(num):
    print(first)
    temp=first
    first=second
    second=second+temp

