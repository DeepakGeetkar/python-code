# #####################  class and object #############

# class Demo:                      # alweys class difine in capital letter
#     print("hello")               # body of class 

# c=Demo()                         # object of class 

# ###########################  constuter ##############

# class demo:
#     def __init__(self):                    # constuer call by self 
#         print("its a constuter ")

#     def myFunction(self):                   # methods call by caliing in object
#         print("its a function/ or method")

# c=demo()                                   #class calling and object of class
# c.myFunction()                             # method calling



############################################################

# class Myclass:                                                                   # class
    
#     def __init__(self,name,age):                                                # constuter
#         self.name=name
#         self.age=age

#     def myFunction(self):                                                       # method
#         # self.name="raja"
#         # self.age=20
#         print(f" my name is {self.name} and my age is {self.age}")


# c=Myclass("rama",15)                                              # object criated for class
# c.age=40                                                          # update age
# c.myFunction()                                                   # calling object  my function


class Myclass:                                                                  
    name="raja"                 ## class insitance                    
    age=20
    def __init__(self):                                                
        print(" its constuter")


    def myFunction(self,name,age):                                             
        self.name="raja"        # method  insitance
        self.age=20
        print(f" my name is {self.name} and my age is {self.age}")
