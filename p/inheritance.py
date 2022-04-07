#############################################################################################################
######## INHERITANCE########
# single inheritance
# class Parentclass:                                      #class
    
#     def myFunction1(self):                              # methods
#         print("perent class function called")

#     def showDeatils(self,name,age):                     # methods overriding
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}year")

# class Childclass(Parentclass):                          #child class
    
#     def myFunction2(self):                               # method
#         print("child class function called")

#     def showDeatils(self,name,age):                       #method overrrding
#         self.name=name
#         self.age=age
#         print(f"my name is {self.name} and my age is {self.age}year")

# # c=Childclass()                #object of child class
# # c.myFunction1()               # function call by using child class 
# # c.myFunction2()
# # c.showDeatils("ram",30)       # method overreding using child class objcet
# # c.showDeatils("deepak",)

# p=Parentclass()                 # peran\t class object
# p.showDeatils("seema",18)       # method overriding using paarent classs object



#########################################################################################################
# multilevel  inheritance
# class A:
    
#     def myFunction1(self):
#         print(" class A function called")

    

# class B(A):
    
#     def myFunction2(self):
#         print("class B function called")

    

# class C(B):
    
#     def myFunction3(self):
#         print("class C function called")

    

# c=C()
# c.myFunction2()
# c.myFunction1()
# c.myFunction3()



########################################################################################################
## multiple inheritance

# class A:
    
#     def myFunction1(self):
#         print(" class A function called")

    

# class B:
    
#     def myFunction2(self):
#         print("class B function called")

    

# class C(A,B):                                         # inherit by class A and classB
    
#     def myFunction3(self):
#         print("class C function called")

    

# c=C()
# c.myFunction2()
# c.myFunction1()
# c.myFunction3()      
#b=B()
#.myFunction1()           # throw error becouse class b is not inherit by class a




#############################################################################################################
# hierarchial inheritance
# class A1:                                          #perent class
    
#     def myFunction1(self):
#         print(" class A function called")

    

# class B1(A1):                                          #1st child class inherit by pernt class
    
#     def myFunction2(self):
#         print("class B function called")

    

# class C1(A1):                                         #2nd childclass inherit by perent class
    
#     def myFunction3(self):
#         print("class C function called")

    
# c=C1()                                               # object child class c
# c.myFunction1()
# c.myFunction3()
# b=B1()                                               #object child class b
# b.myFunction1()
# b.myFunction2()



###########################################################################################################
# hybrid inheritance
# class A1:                                          #perent class
    
#     def myFunction1(self):
#         print(" class A function called")

    

# class A2(A1):                                          #1st child class inherit by pernt class
    
#     def myFunction2(self):
#         print("class B function called")

    

# class A3(A1):                                         #2nd childclass inherit by perent class
    
#     def myFunction3(self):
#         print("class C function called")



# class A4(A2,A3):                                         #3rd childclass inherit  1st child class and 2nd child class
    
#     def myFunction4(self):
#         print("class d function called")

# a=A4()                                                     # object of child class
# a.myFunction1()                                            # run call class 
# a.myFunction2()
# a.myFunction3()
# a.myFunction4()


################################################################################################################################

################## POLYMORPHISM ################
# METHOD OVERLODING :- YYH PYTHON ME SUPORT NHI KRTI H

class MO:
    def myFunction(self):                          #no arugument function
        print("function with no arugument")

    
    def myFunction(self,a):                          
        print("function with 1 arugument")

    def myFunction(self,a,b):                          
        print("function with 2 arugument")

m=MO()
m.myFunction3(10,20)
#m.myFunction(10)