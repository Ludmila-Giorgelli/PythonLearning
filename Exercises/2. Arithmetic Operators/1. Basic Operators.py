# Codes for EXERCISE 1

# Code for (1) AND (2)
Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter another number: "))
sub = Num2 - Num1
print(sub)

# Code for (3)
Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter another number: "))
Div = Num1/Num2
print(Div)

# Code for (4)
Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter another number: "))
Mult = Num1*Num2
print(Mult)

# Code for (5)
Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter another number: "))
if Num1 > Num2:
    print(Num1, " Es mayor")
else:
    print(Num2, " Es mayor")

# Code for (6)
Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter another number: "))
print(pow(Num1, Num2))

# Code for EXERCISE (2)
street_number = int(input("Enter your current street number: "))
destination = 1800
blocks = int(abs(destination - street_number)/100)
if street_number % 100 == 0 and street_number < 1800:
    print("there are {} blocks left".format(blocks))
if street_number % 100 == 0 and street_number > 1800:
    print("You should go back {} blocks".format(blocks))
else:
    print("Te fuiste mono ")