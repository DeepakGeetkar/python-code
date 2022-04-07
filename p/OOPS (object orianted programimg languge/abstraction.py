# ABSTRACTION : abstrsction is using to hide the data in the clsss like exmple mouse== in iner side of mouse we dosnt 
# know what are doing so in that type mouse we called abstraction.  in a class we make abstraction methods and in there 
# no presnt a body of class. in abstrsction methed complcesy to inheritance and onather class is also make those methed


# from abc import (ABC,abstractmethod)
# class Shape(ABC):                             #abstraction class
#     @abstractmethod
#     def aera(self):                      # abstraction method
#         pass
#     @abstractmethod
#     def peramiter(self):
#         pass
#     def __init__(self,name):
#         self.name=name

# class Circle(Shape):
#     def __init__(self,radius):
#         super().__init__(Circle)
#         self.radius=radius

#     def aera(self):
#         return 3.14*(self.radius**2)

#     def peramiter(self):
#         return 2*3.14*self.radius

# class Rectangle(Shape):
#     def __init__(self,length,width):
#         super().__init__(Rectangle)
#         self.lenght=length
#         self.width=width

#     def aera(self):
#         return self.width*self.lenght

#     def peramiter(self):
#         return 2*(self.width+self.lenght)



# c=Circle(5)
# r=Rectangle(10,20)
# print(c.aera())
# print(c.peramiter())
# print(r.aera())
# print(r.peramiter())
# print(c.name)
# print(r.name)


###############################################################################################
class RBI:
    def intrest(self):
        pass

class SBI(RBI):
    def intrest(self):
        print("intersent rate of sbi is 9%")

class PNB(RBI):
    def intrest(self):
        print("intersent rate of pnb is 7%")

class HDFC(RBI):
    def intrest(self):
        print('intersent rate of hdfc is 5%')


h=HDFC()
p=PNB()
s=SBI()
h.intrest()
p.intrest()
s.intrest()