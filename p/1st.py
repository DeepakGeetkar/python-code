########## using object call and method call 



# class clecey:
#     def sum(a,b):
#         #a=5
#         #b=9
#         print(a+b)
#     def sub(a,b):
#         #a=10
#         #b=5
#         print(a-b)
#     def mul(a,b):
#         #a=6
#         #b=6
#         print(a*b)
#     def div(a,b):
#         #a=400
#         #b=20
#         print(a/b)
#     #sum()     #without oject function or module call
#     #sub()
#     #mul()    
#     #div()
# a=int(input("enter the value of num"))
# b=int(input("enter the value of num"))
# clecey.sum(a,b)
# clecey.sub(a,b)    
# clecey.mul(a,b)    
# clecey.div(a,b)   

##### create a vechial class with max_speed and milage
# class Vehicle:
#     def __init__(self,max_speed,milage):
#         self.max_speed = max_speed
#         self.milage = milage



# c=Vehicle(100,30)
# #print(modelX.milage,modelX.max_speed)
# print(c.max_speed)
        
        
########## vehicle to bus class
# class Vehicle:                  #class



#     def __init__(self,name,max_speed,milage):         #initmethod
#         self.name=name
#         self.max_speed=max_speed
#         self.milage=milage


# class Bus(Vehicle):                                            #child class
#      def opreter(self,Name,mobile_number,id_card):
#          self.Name=Name
#          self.mobile_number=mobile_number
#          self.id_card=id_card


# school_bus= Bus ("school volvo",180,40)                         #object in child class
# school_bus.opreter("ram",9989786769,121)
# print(school_bus.name)
# print(school_bus.Name,school_bus.mobile_number,school_bus.id_card)
# print(school_bus.max_speed)
# print(school_bus.milage) 





############  area of cricule and formula == 3.14*radius**2 and perimter=2*3.14*radius
# class cricle:

#     def __init__(self,radius):
#         self.radius=radius
#     def getArea(self):
#         return 3.14*self.radius*self.radius

#     def getCirumference(self):
#         return 2*self.radius*3.14

#     #getArea("6")
#     #getCirumference(5)
# c=cricle(6)
# print(c.getArea())
# print(c.getCirumference())  


####################### aera of Rectangle################## formula aera= lenghth*width and perametr is =2(l+w)
# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width

#     def aera(self):
#         return self.length*self.width

#     def perameter(self):
#         return 2*(self.length+self.width)

# r=Rectangle(10,20)
# print(r.aera())
# print(r.perameter())



################################# aera of tringle ##########################
class Tringle:
    def __init__(self,side,base,hight):
        self.side=side
        self.base=base
        self.hight=hight
    def aeraTringle(self):
        return (self.hight*self.base)//2
    def perameter(self):
        return (self.hight+self.base+self.side)

t=Tringle(10,10,10)
print(f" aera of tringle {t.aeraTringle()}")
print(f" peramiter of tringle {t.perameter()}")
