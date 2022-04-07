# num=int(input("enter your number"))
# sum=0
# temp=num
# while temp>0:
    # digit=temp%10
    # sum+=digit**3
    # temp//=10
# if num==sum:
    # print(f"given num is {num} amstrong number ")
# else:
    # print(f"given num is {num} not amstrong number ")












num=int(input("num"))
sum=0
temp=num
n=len(str(num))
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if sum==num:
    print("amstrong")
else:
    print("not amstrong")