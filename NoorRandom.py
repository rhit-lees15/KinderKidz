# Hello World

# Test Code
## Noor

# Import string and random module
import string
import random
 
# Randomly choose a letter from all the ascii_letters
# randomLetter = random.choice(string.ascii_letters)
# print(randomLetter)

# Import random module -- no need for repetition
## import random
 
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
#wordList = ['BATH', 'CARE', 'LOVE']
randomWord = random.choice(wordList)
print(randomWord)

remainingLetters = 8 - len(randomWord)
#print(remainingLetters)
 
# If we want to randomly generate a ascii value from 'A' to 'Z':
while remainingLetters > 0:
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    print(randomUpperLetter)
    remainingLetters -= 1