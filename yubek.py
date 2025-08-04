
weight=float(input("enter weight in kg"))
height=float(input("enter height in inches:"))

height_in_meters= height *0.0254

print(height_in_meters)

bmi = weight / (height_in_meters)**2
print(f"bmi is {round(bmi,3)} ")

if (bmi>12 and bmi<18.5):
    print("you are under weight")
elif (bmi>=18.5 and bmi<25):
    print("you are healthy")
elif (bmi>=25 and bmi<30):
    print("you are over weight")
elif (bmi>=30 and bmi<50):
    print("you are obesity")
else:
    print("bmi is not inside range.Correct value not provided")


cost_price=float(input("enter cost price"))
selling_price=600

profit = selling_price-cost_price
