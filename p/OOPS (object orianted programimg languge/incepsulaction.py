# incepsulaction :- incepsulaction is method to variable and method is using in a cepsul
# there are two type 1- protected(_) and 2- privet(__)
# privet method
class A:
    def __init__(self,a):
        self.__a               # the variable is privet

    def show(self):
        print("privet variable",self.__a)

class B(A):
    def __init__(self,b):
        super().__init__(b)               # the variable is privet

    def show(self): v  
        print(self.__a)

b=B(20)
b.show()
