# Hello World

# Test Code Method 1
## Noor

# Import string and random module
import string
import random
 
# Should we wish to randomly choose a lower case letter
# randomLetter = random.choice(string.ascii_letters)
# print(randomLetter)

def generateRandomWord(words):
    return random.choice(words)

wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
#wordList = ['BATH', 'CARE', 'LOVE']
randomWord = generateRandomWord(wordList)
print(randomWord)

remainingLetters = 8 - len(randomWord)
#print(remainingLetters)
 
# If we want to randomly generate a ascii value from 'A' to 'Z':
while remainingLetters > 0:
    randomUpperLetter = chr(random.randint(ord('A'), ord('Z')))
    print(randomUpperLetter)
    remainingLetters -= 1
