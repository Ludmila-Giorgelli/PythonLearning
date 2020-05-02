
# Code for (1)

# Metodo 1 -> Usando mal la condicion del while y el break.
# import random
#
# number = random.randint(1, 3)
# guessTaken = 0
# print("Think of a number between 1 and 10: ")
#
# while guessTaken != number:
#     guessTaken = int(input("Ingrese un numero: "))
#     if guessTaken == number:
#         print("Good job, you guessed the number")
#         break
#     if guessTaken != number:
#         print("Try again")

# Metodo 2 -> Usando unicamente el break y pasando "TRUE" a la condicion del while
# import random
# max = 3
# number = random.randint(1, max)
# guessTaken = 0
# print("Think of a number between 1 and {}: ".format(max))
#
# while True:
#     guessTaken = int(input("Ingrese un numero: "))
#     if guessTaken == number:
#         print("Good job, you guessed the number")
#         break
#     if guessTaken != number:
#         print("Try again")

# Metodo 3 -> Usando bien la condicion del while y sin "Break"
# import random
# max = 3
# number = random.randint(1, max)
# guessTaken = 0
# print("Think of a number between 1 and {}: ".format(max))
#
# keepRunning = True
#
# while keepRunning:
#     guessTaken = int(input("Ingrese un numero: "))
#     if guessTaken == number:
#         print("Good job, you guessed the number")
#         keepRunning = False
#     if guessTaken != number:
#         print("Try again")