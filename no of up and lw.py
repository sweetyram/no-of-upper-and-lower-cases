str1 = "The quick Brow Fox"
upper = 0
lower = 0
for i in str1:
    if (i.isupper()):
        upper += 1
    else :
        lower +=1
print("the no of upper case character is :",upper)
print("the no of lower case character is :",lower)