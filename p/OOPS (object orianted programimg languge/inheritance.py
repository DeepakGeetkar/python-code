#############################  inheritance ###############################

##### single inheritance
# class Compny:
#     def name(self):
#         print("my name is rohan")

# class Employe(Compny):                        # single inheritance
#     def salary(self):
#         print("salary of employe is 20k")

# e=Employe()
# e.name()
# e.salary()

###########################################################################################

######    multilevel inheritance

# class Compny:                               #perent class
#     def name(self):
#         print("my name is rohan")

# class Employe(Compny):               #sub perent class inherit by perent          # multilevel inheritance
#     def salary(self):
#         print("salary of employe is 20k")

# class Department(Employe):         # child class inherit by sub perent class               # multilevel inheritance
#     def maintance(self):
#         print("i am in maintance depaetment ")

# d=Department()
# d.name()
# d.salary()
# d.maintance()

###################################################################################

## multiple inheritance

# class Compny:                          # perent class
#     def name(self):
#         print("my name is rohan")

# class Employe():                        # sencod perent class      
#     def salary(self):
#         print("salary of employe is 20k")

# class Department(Compny,Employe):       # child class inherit by both perent class                # multiple inheritance
#     def maintance(self):
#         print("i am in maintance depaetment ")

# d=Department()
# #e=Employe
# d.name()
# d.salary()
# d.maintance()

#######################################################################################3

# herachical inheritance

# class Compny:
#     def name(self):                                   # perent class
#         print("my name is rohan")

# class Employe(Compny):             # child class inherit by perent                  # herachial inheritance
#     def salary(self):
#         print("salary of employe is 20k")

# class Department(Compny):           # child class inhert by perent              # herachical  inheritance
#     def maintance(self):
#         print("i am in maintance depaetment ")

# d=Department()
# e=Employe()
# d.name()
# d.maintance()
# e.name()
# e.salary()


##########################################################################################33

## hybrid inheritance

class Compny:
    def name(self):                                   # perent class
        print("my name is rohan")

class Employe(Compny):             # sub class inherit by perent                  # herachial inheritance
    def salary(self):
        print("salary of employe is 20k")

class Department(Compny):           # subchild class inhert by perent              # herachical  inheritance
    def maintance(self):
        print("i am in maintance depaetment ")

class Workingday(Employe,Department):           # child class inhert by perent              # herachical  inheritance
    def weekly(self):
        print(" my working day 6 in a week ")

w=Workingday()
w.weekly()
w.name()
w.maintance()
w.salary()