####  ase string jinka speling smman ho pr minig alg alg ho exmp== roket and kroet  or night and hignt

# str1=input("enter your str1")
# str2=input("enter your str2")
# 
# sorted_str1= sorted(str1)
# sorted_str2= sorted(str2)
# 
# if sorted_str1==sorted_str2:
    # print("given string is anagram ")
# else:
    # print("given string is not anagram")

#########################################################################
# anargam number using len method
str1=input("enter your str1")
str2=input("enter your str2")
# 
# sorted_str1= sorted(str1)
# sorted_str2= sorted(str2)

if len(str1)==len(str2):
    if sorted(str1)==sorted(str2):
        print("given string is anagram ")
    else:
        print("given string is not anagram")
else:
    print("given string is not a anagram")