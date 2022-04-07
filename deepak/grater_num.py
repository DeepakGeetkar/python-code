#print("hello world")

###### odd evan program
# num= int(input("enter your num"))
# if num%2==0:
#     print("evan")
# else:
#     print("odd") 



num1= int(input("enter your num1\n"))
num2= int(input("enter your num2\n"))
num3= int(input("enter your num3\n"))
def muxmium(num1,num2,num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=muxmium(num1,num2,num3)
print(m,"the number is highest in givens number")
