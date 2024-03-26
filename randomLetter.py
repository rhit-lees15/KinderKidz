# Test Code 2 - Random Letter & Word Generator

import string
import random

# function to choose a random word from an imported list of words
def generateRandomWord(words):
    return random.choice(words)

wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
#wordList = ['BATH', 'CARE', 'LOVE']
randomWord = generateRandomWord(wordList)

# function to generate additional random letters as necessary by the 
# length of the word chosen

# 8 because we only have 8 tiles for letters
remainingLetters = 8 - len(randomWord)

def generateRandomLetters(remainingLetters):
    # ensure no repeated letters:
    availableLetters = string.ascii_uppercase
    chosenLetters = random.sample(availableLetters, remainingLetters)
    return ''.join(chosenLetters)
    return ''.join(random.choices(string.ascii_uppercase, k=remainingLetters))

randomLetters = generateRandomLetters(remainingLetters)

# function to add all of the letters to one singular string

def randomizeLetters(word, letters):
    allLetters = list(word + letters)
    random.shuffle(allLetters)
    return ''.join(allLetters)

randomizedLetters = randomizeLetters(randomWord, randomLetters)

print("Selected Word:", randomWord)
print("Random Letters:", randomLetters)
print("Randomized Letters", randomizedLetters)