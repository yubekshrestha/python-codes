# #  import randomas raise

# message= input("enter the an string you want:")
# reversedmessage=""
# i = len(message) -1
# while i >= 0:
#     reversedmessage += message[i]
# print("resersedmessage")


# luckynumber = r.randint(0, 10)
# print(luckynumber)

# message = " ahtserhs kebuy"

# print(len(message))
# reversedmessage = ""
# for i in range(len(message) -1 , -1 , -1):
#     reversedmessage += message[i]

# print(reversedmessage)


# message = str(input("enter the string variable"))

# print(len(message))
# reversedmessage = ""
# for i in range(len(message) -1 , -1 , -1):
#     reversedmessage += message[i]

# print(reversedmessage)

# palindrome number
# number = int(input("Enter the number you want to check the palindrome of:"))
# number2= number
# reverse_num = 0

# while(number2>0):
#     remainder = number2%10
#     reverse_num=reverse_num*10 + remainder
#     number2=int(number2/10)
# print(reverse_num)

# if(reverse_num==number):
#     print("The number is palindrome")
# else:
#     print("The number is not palindrome")


# number = int(input("Enter the number"))
# number2=number
# digit_count=0
# sum=0
# while number2>0:
#     digit_count += 1
#     number2 =int(number2/10)
# print(digit_count)
# number2=number
# while(number2>0):
#     remainder=number2%10
#     sum +=remainder**digit_count
#     number2=int(number2/10)
# print(sum)
# if(sum == number):
#     print("The number is armstrong")
# else:
#     print("The number is not armstrong")


# number=int(input("enter the number which you want(5 digiit):"))
# number2= number
# sum=0

# while number2>0:
#     sum += (number2%10)**5
#     number2 = int(number2/10)
# if( sum == number):
#     print("this a armstrong")
# else:
#     print("this is not armstrong")


# number = int(input("enter the factorial number"))
# factorial=1
# for i in range(1,number+1):
#     factorial *= i
# print("factorial",factorial)

# i=1
# while i<=number:
#     factorial *= i
#     i +=1
# print("factorial",factorial)


# number = int(input("enter the fibonacci number you want:"))
# a=0
# b=1
# print(a , b , end =" ")
# for i in range(0,number-2):
#     c = a + b
#     print(c , end=" ")
#     a=b
#     b=c
# print("")
# difference<2:very close
# 2<difference<5:close
# 5<difference<10:far
# difference>10: veryfar

# import random
# answer = int(random.random()*50)
# while True:
#     number = int(input("enter a number to guess from 1 to 50 or input 51 to cancel"))
#     if number==51:
#         break
#     if number==answer:
#         print("You guessed right. New number has been generated guess again.")
#         answer=int(random.random()*50)
#     elif abs(number-answer) <=2:
#         print("you are very close")
#     elif 2<abs(number-answer)<=5:
#         print("you are close")
#     elif 5<abs(number-answer)<=10:
#         print("you are far")
#     elif abs(number-answer)>10:
#         print("you are very far")
#     else:
#         print("You are wrong!")


# import random
# answer = random.randint(0, 50)
# while True:
#     number = int(input("enter a number to guess from 1 to 50 or input 101 to cancel"))
#     if number==101:
#         break
#     if number==answer:
#         print("You guessed right")
#     elif abs(number-answer) >5:
#         print("you are far")
#     elif abs(number-answer)<=5:
#         print("you are close")
#     else:
#         print("You are wrong!")


# import random
# answer = random.randint(0 , 50)
# while True:
#     number = int(input("enter a number to guess from 1 to 50 or input 101 to cancel"))
#     if number==101:
#         break
#     if number==answer:
#         print("You guessed right")
#     elif abs(number-answer) >5:
#         print("you are far")
#     elif abs(number-answer)<=5:
#         print("you are close")
#     else:
#         print("You are wrong!")

# prime factors

# number = int(input("Enter a number:"))

# while number % 2 == 0:
#     print("2", end=" ")
#     number = int(number / 2)
# i = 3
# while i**2 <= number:
#     while number % i == 0:
#         print(i, end=" ")
#         number = int(number / i)
#     i+=2
# if(number>2):
#     print(number)
# print("")



# import random as r

# papar = 1
# rock = 2
# scissor = 3

# while True:
#     answer = r.randint(1,3)
#     print( 
#            '''
# enter your choice:
# 1. paper
# 2. rock
# 3. scissor
# 4. exit
          
#          '''
# )
# userinp= int(input("enter your choice:"))
# if userinp == 4:
#     break
# if userinp > 4 or userinp <= 0 :
#     print("wrong choice")
# elif answer == userinp == 1:
#     print("both choice paper")
# elif answer == userinp == 2:
#     print("both choice rock")
# elif answer == userinp == 3:
#     print("both hoice scissor")
# elif userinp == 1:
#     if answer == 2:
#        print("you choice paper. opp choice rock. you win")
#     elif answer == 3:
#         print("you choice paper. opp choice rock.you lose")  
# elif userinp == 2:
#     if answer == 1:
#         print("you choice rock. opp choice paper. you  lose")
#     elif answer == 3:
#         print("you choice rock. opp choice scisspr. you win")    
# elif userinp == 3:
#     if answer == 1:
#         print("you choise scissor. opp choice paper. You win")
#     elif answer == 2:
#         print("you choice scissor. opp choice rock. you lose")
  
  
  
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
          
          """)
    
    
number = int(input("enter the number between 1 to 4:"))
value1= r.andint(0,100)
value2 = r.randint(0,100)

print(f" random value : (value1) and (value2)")


if number == 1:
    result = value1 + value2
    print(f"add result: (value1) + (value2) = (result)")
elif number == 2:
    result = value1 - value2
    print(f"sub result:(result)")
elif number == 3:
    result = value1 / value2
    print(f"divi result:(result)")
elif number == 4:
    result = value1 * value2
    print (f"multi result:(result)")
else:
    print(" above 5 number is invalid")

