# Test Code 2 - Random Letter & Word Generator

import string
import random

# function to choose a random word from an imported list of words
def generateRandomWord(words):
    return random.choice(words)

wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
#wordList = ['BATH', 'CARE', 'LOVE']
randomWord = generateRandomWord(wordList)

print("Selected Word:", randomWord)

# function to generate additional random letters as necessary by the 
# length of the word chosen

# 8 because we only have 8 tiles for letters
remainingLetters = 8 - len(randomWord)

print("Letters To Fill:", remainingLetters)

def removeLetters(letters2Remove):
    alphabet = list(string.ascii_uppercase)
    
    for letter in letters2Remove:
        if letter in alphabet:
            alphabet.remove(letter)
    alphabetString = ''.join(alphabet)
    return alphabetString

letters2Remove = randomWord
availableLetters = removeLetters(letters2Remove)

print("Left Over Letters:", availableLetters)

## remove possibility of repeating letter by removing the randomly chosen letters from the list

def generateRandomLetters(remainingLetters):
    # ensure no repeated letters:
    chosenLetters = random.sample(availableLetters, remainingLetters)
    return ''.join(chosenLetters)
    return ''.join(random.choices(string.ascii_uppercase, k=remainingLetters))
    
randomLetters = generateRandomLetters(remainingLetters)

print("Random Letters:", randomLetters)

# function to add all of the letters to one singular string

def randomizeLetters(word, letters):
    allLetters = list(word + letters)
    random.shuffle(allLetters)
    return ''.join(allLetters)

randomizedLetters = randomizeLetters(randomWord, randomLetters)

print("Final Letter Sequence:", randomizedLetters)