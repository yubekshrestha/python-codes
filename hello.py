no1=int(input('enter first number'))
no2=int(input('enter second number'))

add_result = no1 + no2
sub_result = no1-no2
multi_result = no1 * no2
divi_result = float(no1)/float(no2)
reminder_result = no1%no2
square1=no1**2
sqaure2=no2**2



print("additiom is " + str(add_result))
print(f"sub is {sub_result}") 
print(f"mult is {multi_result}\ndivi is {divi_result}")
print(f"reminder is {reminder_result}")
print(f"sqaure of {no1} is {square1}")
print(f"sqaure of {no2} is  {sqaure2}")


# format method in python

text = '''
This is a long text in python.
It is a multiline text.
My name is {name}
I live in {city}, {country}
I have Rs{:,}
I have Rs{:_}

'''

print(text.format(500000,100000, city="Kathmandu", country="nepal",name="yubek"),"hello")

