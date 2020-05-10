# Code for 4.1.1

# def addNumbers(num1: int, num2: int) -> int:
#     result = num1 + num2
#     return result
#
#
# def substractNumbers(num1: int, num2: int) -> int:
#
#     return num2 - num1
#
#
# def divideNumbers(num1: int, num2: int) -> float:
#
#     return num1 / num2
#
#
# def multiplyNumbers(num1: int, num2: int) -> int:
#      return num1 * num2
#
#
# def getHighestNumber(num1: int, num2: int) -> int:
#
#     if num1 > num2:
#         highest = num1
#     else:
#         highest = num2
#
#     return highest
#
#
# def byThePowerNumbers(num1: int, num2: int) -> int:
#
#     return pow(num1, num2)

# Code for  4.1.2

# import random
#
# def guessRandomNumber(maxnum: int, maxTries: int) -> bool:
#     randomNumber = random.randint(1, maxnum)
#     tryCount = 0
#     inputText = "Please enter a number: "
#     print("Think of a number between 1 and {}. You have {} {}".format(maxnum, maxTries, getRightWord(maxTries)))
#
#     while True:
#         guess = int(input(inputText))
#         tryCount += 1
#
#         # if guess == randomNumber and tryCount < maxTries:
#         if guess == randomNumber:
#             print("Good job, you guessed the number in {} {}".format(tryCount, getRightWord(tryCount)))
#             return True
#
#         if tryCount >= maxTries:
#             print("You guessed wrong and ran out of max tries")
#             return False
#
#         if guess != randomNumber and tryCount < maxTries:
#             # print("You guessed wrong. Try again")
#             remainingTries = maxTries - tryCount
#             inputText = "You guessed wrong. {} {} left. \nTry again: ".format(remainingTries, getRightWord(remainingTries))
#
#
# def getRightWord(tries: int):
#     if tries == 1:
#         return "try"
#     else:
#         return "tries"
#
#
# guessRandomNumber(1, 2)


# Code for 4.1.3

# import time
#
#
# def countdown(num: int):
#
#     for x in range(num):
#         time.sleep(1)
#         print(num - x)
#
#
# countdown(10)

