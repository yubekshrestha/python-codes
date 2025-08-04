import random as r

add = 1
sub = 2
divi = 3
multi = 4

while True:
    print(""" 
choice the number between them
 1. add
 2. sub
 3. divi
 4. multi
 5. Exit
          
          """)
    number = int(input("enter the number between 1 to 4:"))
    
    
    if number == 5:
        break
    elif number >5 or number <1:
        print(" above 5 or less than 1 number is invalid")
        break
    # if number == 5 :
        # break
    value1=int(input("Enter the first number:"))
    value2=int(input("Enter the second number:"))
    if number == 1:
        result = value1 + value2
        print(f"add result: {value1} + {value2} = {result}")
    elif number == 2:
        result = value1 - value2
        print(f"sub result:{result}")
    elif number == 3:
        result = value1 / value2
        print(f"divi result:{result}")
    elif number == 4:
        result = value1 * value2
        print (f"multi result:{result}")


