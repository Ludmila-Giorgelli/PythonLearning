
# Code for (1)

import random
guessesTaken = 0

number = random.randint(1, 10)
print("Think of a number between 1 and 10: ")

while guessesTaken<11:
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess == number:
        print ("Good job, you guessed the number")
        break
    if guess != number:
        print("Try again")
