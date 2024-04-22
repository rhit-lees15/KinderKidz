import RPi.GPIO as GPIO
import string
import random
import time

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Function to generate a random word
def generateRandomWord(words):
    return random.choice(words)

# Function to generate additional random letters
def generateRandomLetters(remainingLetters, numLetters):
    return random.sample(remainingLetters, numLetters)

# Function to add all letters to one string and shuffle them
def randomizeLetters(word, letters):
    allLetters = list(word + ''.join(letters))
    random.shuffle(allLetters)
    return ''.join(allLetters)

# Function to handle button press event
def buttonPress(pin):
    global spelledWord, randomWord, randomizedLetters
    
    letter = button_letters[pin]
    if len(spelledWord) < len(randomWord) and letter == randomWord[len(spelledWord)]:
        spelledWord += letter
        print("Current spelling:", spelledWord)
    else:
        print(f"Incorrect! Button {pin} is not the next letter or the word is complete. Try again.")
    
    if len(spelledWord) == len(randomWord):
        if spelledWord.upper() == randomWord:
            print("Correct! You spelled the word correctly.")
            newWord()
        else:
            print("Incorrect! Try again.")
            spelledWord = ''

# Function to generate and display a new word
def newWord():
    global spelledWord, randomWord, randomizedLetters
    randomWord = generateRandomWord(wordList)
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    spelledWord = ''
    displayLetters(randomWord, button_letters)

# Function to display the available letters
def displayLetters(word, letters):
    print("Available letters: ", end="")
    for letter in word:
        print(letters[letter], end=" ")
    print()

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=200)

# Generate a random word
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(wordList)

# Get remaining letters
availableLetters = list(set(string.ascii_uppercase) - set(randomWord))

# Generate additional random letters
randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))

# Combine the random word and random letters into a single string and shuffle them
randomizedLetters = {}
for idx, letter in enumerate(randomWord):
    randomizedLetters[letter] = letter
for letter in randomLetters:
    randomizedLetters[letter] = letter

# Map each letter to a button
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    if idx < len(randomWord):
        button_letters[pin] = randomWord[idx]
    else:
        button_letters[pin] = randomLetters[idx - len(randomWord)]

# Start the game
print("Welcome to the Word Spelling Game!")
print(f"Spell the word: {randomWord}")
displayLetters(randomWord, button_letters)

spelledWord = ''

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
