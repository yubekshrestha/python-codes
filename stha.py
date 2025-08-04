cp=float(input("enter the cost price"))
sp=float(input("enter the selling price"))

profit=sp-cp

print("proft or loss")
if (sp>cp):
    print("it is a profit")
elif (sp<cp):
    print("it is a loss")
else:
    print(" neither profit or loss")

text = '''
 its me {name}
 is my coding correct ????
 monthly income {salary}
'''
print(text.format(name="yubek",salary=50000),"hello guysss")

