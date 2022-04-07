############# find given string is anagram or not 



# str1=input("enter your str1:")
# str2=input("enter your str2:")

# sorted_str1= sorted(str1)
# sorted_str2= sorted(str2)

# if sorted_str1==sorted_str2:
#     print("given string is aanagram")
# else:
#     print("givens string is not annagram")


########### FIND GIVEN NUMBER IS PALINDROM NUMBER
# string= int(input("enter your string"))
# reversd = int(str(string)[::-1])
# if string==reversd:
#     print("given string is palindrom")
# else:
#     print("given string is not palindrom")


######## factrorial 

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
n= int(input('enter your number'))
result=factorial(n)
print("the given num is",n,'and is fatorial is ',result)