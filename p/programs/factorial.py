# num=int(input("enter your num"))
# result=1
# for i in range(num,0,-1):
    # result= result*i
# print(f"{num} is  and {result} factorial")






def factorial(num):
    if num==0:
        return 1
    else:
        return num*factorial(num-1)
num=int(input('enter your number'))
result=factorial(num)
print(f"the num is {num} and factorial of the number is {result}")