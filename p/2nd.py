####### using a class method create a program to given a odd even nuber or a leap year


# class Number:         #creatiag a class
#     def odd_even(num):                                        # method 1st
#         if num%2==0:
#             print("even")
#         else:
#             print("odd")
#     def leapyear(year):                                       # method 2nd
#         if (year%4==0 or year%400==0) and (year%100!=0):
#             print(year,"given year is leap year")
#         else:
#             print(year,"given year is not a leap year")
#     #odd_even(5)                                                #using method call 
#     #leapyear(1900)                                             # using method call
# Number()  ## creating a object 
# Number.odd_even(6)                                              #using object call
# Number.leapyear(2020)                                           #using object call





####### USING CLASS OBJECT METHOD MAKE A PROGRM TO 
class MyPrograms:                                                      # class
    def primenumber(num):                                              # method
        for i in range(2,num):
            if num%i==0:
                print(f"given num {num} is not a prime number ")
                break
        else:
            print(f"given num {num} is prime number")

    def factorial(num):                                               # method
        result=1
        for i in range(num,0,-1):
            result=result*i
        print(f"the given number {num} and factorial of this num is {result}") 

    def palindrone(num):                                               #method
        reverse=int(str(num)[::-1])
        print(f"reverse string {reverse} ")
        if num==reverse:
            print(f"{num} is palindrome")
        else:
            print(f"{num} is not palindrome")


    #palindrone(565)                                                        # method call
    #factorial(5)
    #primenumber(15)
    #primenumber(17)
MyPrograms()                                                                 # object
num=int(input("enter your num"))
MyPrograms.primenumber(num)                                                  # object call
MyPrograms.palindrone(num)
MyPrograms.factorial(num)
