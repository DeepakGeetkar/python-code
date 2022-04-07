###################amstrong ################

#num= int(input('num'))
# sum=0
# temp=num
# Num=len(str(num))
# while temp>0:
    # digit=temp%10
    # sum +=digit**Num
    # temp//=10
# if sum==num:
    # print("amstrong")
# else:
    # print("not amstrong")

############## palindrome############## 
# reverse=int(str(num)[::-1])
# print("reverse string",reverse)
# if reverse== num:
    # print("palindom")
# else:
    # print("not pdm")
##### anagram##############
# str1=input("str1")
# str2=input("str2")
# 
# if len(str1)==len(str2):
    # if sorted(str1)==sorted(str2):
        # print("anagram")
    # else:
        # print("not anagrm")
# else:
    # print("not anagram")

############### fibonassi serise#####
# num=int(input("num"))
# firist=0
# seccond=1
# for i in range(firist,seccond+1):
    # for i in range(num):
        # print(firist)
        # temp=firist
        # firist=seccond
        # seccond=seccond+temp

############# prime number##########
# 
# num=int(input("num"))
# for i in range(2,num):
    # if num%i==0:
        # print("not prime")
        # break
# else:
    # print("prime")

########### factorial####
num=int(input("num"))
# def fatorial(num):
    # if num==0 or num==1:
        # return 1
    # else:
        # return num*fatorial(num-1)
# result=fatorial(num)
# print(f"the given num{num} and fact{result}")  
# result=1
# for i in range(num,0,-1):
    # result=result*i
# print(f"{num} and fact{result}")


#############  pattern
for i in range(num,0,1):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i):
        print("*", end=" ")
    print()
    




