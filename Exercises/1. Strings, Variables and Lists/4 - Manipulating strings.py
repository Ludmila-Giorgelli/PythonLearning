# Code for (1)
word = input("Please enter a full word: ")
letter = input("Please enter a single letter: ")
if letter in word:
    print("The word {} has the letter {} on it".format(word, letter))
else:
    print("The word {} does not have the letter {} on it ".format(word, letter))

# Code for (2)
word = input("Please enter a word: ")
print(word.upper())

# Code for (3)
word = input("Please enter a word: ")
letters = len(word)
print("The word {} has {} letters".format(word, letters))

# Code for (4)
sentence = input("Please enter a sentence: ")
word = "dog"
if word in sentence:
    print("The word {} it's in the sentence".format(word))
else:
    print("The word {} it's not in the sentence".format(word))

# Code for (5)
word = input("Please enter a word: ")
list_of_letters = list(word)
print(list_of_letters)
