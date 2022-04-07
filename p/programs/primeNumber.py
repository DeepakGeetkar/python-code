###################
## prime number 



# num=int(input("enter your number "))

# for i in range(2,num):
#     if num%i==0:
#         print("given number is not a prime number")
#         break
# else:
#     print("given num is prime number")


###########################################
### using function find prime number
# def primenumber(num):
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# num=int(input("num"))
# primenumber(num)



##############################################
#take two number with user and find between prime number



lower=int(input("lower number"))
higher=int(input("higher number"))

for num in range(lower,higher+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

