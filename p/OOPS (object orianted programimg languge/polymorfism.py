######################  POLYMORFISME ##############
# THERE ARE TWO TYPE
#  COMPILE TIME POLY. === ( METHOD  OVERLODDING) ITS NOT SUPPORT IN PYTHON
#  RUN TIME POLY.  =-== (METHOD OVERRIDING) ITS SUPPORT

# METHOD OVERLODDING :- IN METHOD VERLODING IS COMPLINE TIME POLYMORFISM AND IN THERE WE MAKE 
                    #   SAME METHOD OF IN A CLASS AND THERE ARGUMENT IS DIFFRENT. AND METHOD OVERLODING 
                    #   WE DOSNT NEED TO INHERITANCE. 

# class MO:
#     def myFunction(self):
#         print("function with no argument")

#     def myFunction(self,a):
#         print("function with 1 argument")

#     def myFunction(self,a,b):
#         print("function with 2 argument")

# m=MO()
# m.myFunction(10)       ## showing erro becouse method overloding is not supoort

##########################################################################################

 # METHOD OVERRIDING :- METHOD OVERRIDING IS RUN TIME POLYMORFISM  IN THERE WE MSKR DIFFRENT CLASS 
                      # AND SAME METHOD IN EACH CLASS WITH SAME ARGUMENTS  AND IN METHOD OVERRIDING 
                      # COMPLUSERY TO USE 

class MO1:
    def myFunction(self,a,b):
        print("class MO1 function called")

class MO2(MO1):
    def myFunction(self,a,b):
       super().myFunction(10,20)                  # phle super method call hogi fir object vali
       print("class MO2 function called")
       super().myFunction(10,20)                  # phle object vali hogi fir super vali

class MO3(MO2):
    def myFunction(self,a,b): 
        super().myFunction(10,20)
        print("class MO3 function called")
        super().myFunction(10,20)

m=MO3()
m.myFunction(10,20)

