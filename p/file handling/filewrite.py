# # f= open("harry.txt","w")
# # a=f.write("harry is bad boy\n")
# # f.close()


# ## handle read write both
# f= open("harry2.txt","r+")
# ##a=f.write("harry is bad boy\n")
# print(f.read())
# f.write("thanku")
# f.close()


#################################
#file two function
f=open("harry2.txt")
f.seek(12)       # method f.seek kha se start krna h is liye
#print(f.tell())         #  isme ye pta chlta h ki nest line me ky
print(f.readline())

f.close()
