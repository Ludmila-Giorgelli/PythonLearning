# Code for (2)
age = int(input("Enter your age: "))
if age > 18:
    print("They are older than 18")
else:
    print("They're younger than 18")

# Code for (3)
age = int(input("Enter your age: "))
if age > 18:
    print("They are older than 18")
if age < 18:
    print("They are younger than 18")
if age == 18:
    print("They are 18 years old")

# Code for (4)
Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
Num3 = int(input("Enter the third number: "))

if Num1 > Num2 and Num1 < Num3:
    print("True")
else:
    print("False")

# Code for (5)
password = input("Enter a password: ")
characters = int(len(password))
if characters > 6 and characters < 10:
    print("Ok")
else:
    print("Not ok")

# Code for (6)
name = input("Enter your name: ")
last_name = input("Enter your last name: ")
hour = int(input("Enter an hour: "))
if hour >= 6 and hour <= 12:
    print("Good morning {} {} ".format(name, last_name))
if hour >= 13 and hour <= 19:
    print("Good afternoon {} {} ".format(name, last_name))
if hour < 23 and hour < 6:
    print("Good evening {} {} ".format(name, last_name))
if hour > 23:
    print("Try again")





