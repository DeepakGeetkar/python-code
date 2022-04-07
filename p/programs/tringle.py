# class Tringle:
#     def __init__(self,side,base,hight):
#         self.side=side
#         self.base=base
#         self.hight=hight
#     def aeraTringle(self):
#         return (self.hight*self.base)//2
#     def perameter(self):
#         return (self.hight+self.base+self.side)
# side=int(input("side"))
# base=int(input("base"))
# hight=int(input("hight"))
# t=Tringle(side,base,hight)
# print(f" aera of tringle {t.aeraTringle()}")
# print(f" peramiter of tringle {t.perameter()}")

class Cat:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a {self.name} and my age is{self.age}"

    def makesound(self):
        print("meow")

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a{self.name} and my age is {self.age}")

    def makesound(self):
        print("bark")

class Monkey:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def info(self):
        print(f"i am a{self.name} and my age is {self.age}"

ca1=Cat("kitty",2.5)
dog=Dog("serru",1.5)
mok=Monkey("ramu",5)
print(dog.info())
