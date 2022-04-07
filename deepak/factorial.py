#num1= int(input("enter your num1\n"))
####### num2= int(input("enter your num2\n"))
##### num3= int(input("enter your num3\n"))
# def factorial_iter(num1):
#     factorial=1
#     for i in range(num1):
#         factorial=factorial*(i+1)
#     return factorial
# f=factorial_iter(num1)
# print(f)

num1= int(input("enter your num1\n"))
def factorial_recursive(num1):
   
    if num1==1 or num1==0:
        return 1
    return num1*factorial_recursive(num1-1)
    
f=factorial_recursive(num1)
print(f)