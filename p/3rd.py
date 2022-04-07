########## attribute in python
# class Empolye:
#     compny="googale"                 ## class attribute
#     salary= 200000


# deepak=Empolye()                       #object call by aclass
# rajni=Empolye()                        #object

# print(deepak.compny)                    # currnt compny
# print(rajni.compny)   

# Empolye.compny="youtube"                # change the class attrtibuts

# print(deepak.compny)                     # update compny
# print(rajni.compny)                     

# deepak.salary=5000                     # difine new arrtibuts in object side(instance attributs)
# #rajni.salary()

# print(deepak.salary)                    # call the arrtibuts
# print(rajni.salary)
# # print(rajni.addres)            #below line thrrow an error  as address in not presnet in instance class


###############################################################################################################
##### self####
# class Employe:
#     compny='google'
#     def getSalary(self,signeture):             #  sef is autometicly difine
#         print("salary is 100k")
#     @staticmethod                             ## using static method ab isme self nhi lgayege
#     def greet():
#         print("good morrnimg, sir")


# harry= Employe()
# harry.getSalary()
# #Employe.getSalary(harry)     # self nhi lagayege to error deta h
# harry.greet()


#####################################################################################################

#### cnsteuctor ###  yh ek spicel function ya method hota h or  ye self or dusre aruguments leta h  ise __init__ se btate h
# class Employe:
#     conpny="googal"


#     def __init__(self,name, salary,subunit):                           ## constucter
#         self.name= name
#         self.salary= salary
#         self.subunit=subunit
#         print("employed is created")

#     def getDetails(self):                                               #method
#         print(f"name of employe {self.name} and salary of employe is {self.salary} and woring profile is {self.subunit}")

# harry=Employe("harry",100,"youtube")
# ##harry=Employe()                                                       #throww error three arugument is missing
# harry.getDetails()






##########################################################################################################################
#####################################################################################################################

### qustions answer
# class Programer:
#     compny="microsoft"

#     def __init__(self,name,product):
#         self.name=name
#         self.product=product

#     def getInfo(self):
#         print(f"name is {self.name} and product is {self.product}")


# harry=Programer("harry","skype")
# alka=Programer("alka","github")
# harry.getInfo()
# alka.getInfo()
   

   ###############################################################################################
#  ### Inheritance ##   single inheritance
# class Employe:                                         
#     compny= "googale"
    
#     def showDeatils(self):                                              #method overriding
#         print(" this is an employed ")

# class prosesser(Employe):                                               # child class   
#     laguage="python"
#     compny="youtube"

#     def getDeatils(self):
#         print(f"the laguage is {self.laguage}")

#     def showDeatils(self):                                  ##method over riding
#         print(" this is an prosesser ")
     
# e=Employe()
# e.showDeatils()
# p=prosesser()
# e.showDeatils()
# p.getDeatils()
# print(p.compny)
# print(e.compny)

#################################################### #################################################
###### multilevel  inheritance 
# class Employe:
#     compny="bestpear"

#     def showDeatils(self):
#         print(f"{self.compny}this is over compny")

# class Employe2:
#     compny="mssl"
#     def progrmer(self):
#         print("this is a progrmer")
        
#     def showDeatils(self):
#         print(f"{self.compny}this is over compny")

# class student(Employe2,Employe):
#     compny="farm"
#     def getData(self):
#         print(f" this is student {self.compny}")

#     def showDeatils(self):
#         print(f"{self.compny}this is over compny")


# # e=Employe
# f=Employe2
# # s=student 
# # s=s.getData()

# s=student()
# s.progrmer()
# s.showDeatils()
# s.getData()

