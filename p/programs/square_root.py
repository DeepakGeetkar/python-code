################### square root ##########################

num=float(input("enter your num"))

num_sqrt=num**0.5

print(f"the given num is {num} and sqrt of numis {num_sqrt}")
print("the square root of %0.0f is %0.3f"%(num,num_sqrt))


########################## using class fibd SQUARE ROOT #################################

num=float(input("enter your num"))
class Sqrt:
    
    def __init__(self,num):
        self.num=num

    def squareRoot(self):
        return num**0.5

s=Sqrt(num)
a=s.squareRoot()
print("the square root of %0.0f is %0.3f"%(num,a))
