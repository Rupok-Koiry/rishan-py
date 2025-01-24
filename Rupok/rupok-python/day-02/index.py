# print("Welcome to the tip calculator")
# bill=float(input("What was the total bill $"))
# split=int(input('How many people to split the bill? '))
# tip=float(input("What percentage tip would you like to give? "))

# calculate = (bill * (1 + tip / 100)) / split

# print(f"Each person should pay {round(calculate,1)}")


# num=(input("Type two digit number: "))
# print(int(num[0])+int(num[1]))


# # 🚨 Don't change the code below 👇
# height =float(input("enter your height in m: ")) 
# weight =float( input("enter your weight in kg: "))
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# bmi=weight/(height*height)
# print(f"BMI: {round(bmi)}")

age=int(input("What is your age? "))
yearsLeft=90-age
monthLeft=yearsLeft*12
weekLeft=yearsLeft*52
daysLeft=yearsLeft*365
print(f"You have {daysLeft} days, {weekLeft} weeks and {monthLeft} months left")