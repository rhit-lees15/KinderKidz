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
    global spelledWord, randomWord, randomizedLetters, button_sequence
    
    letter = button_letters[pin]
    if letter in randomWord:
        spelledWord += letter
        print("Current spelling:", spelledWord)
    else:
        print(f"Incorrect! Button {pin} is not part of the word. Try again.")
    
    if len(spelledWord) == len(randomWord):
        if spelledWord.upper() == randomWord:
            if checkSequence():
                print("Correct! You spelled the word correctly.")
                newWord()
            else:
                print("Incorrect order! Try again.")
                spelledWord = ''
        else:
            print("Incorrect! Try again.")
            spelledWord = ''

# Function to generate and display a new word
def newWord():
    global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
    
    # Generate a new word
    randomWord = generateRandomWord(wordList)
    
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
    
    # Generate additional random letters
    randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))
    
    # Combine the random word and random letters into a single string and shuffle them
    randomizedLetters = randomizeLetters(randomWord, randomLetters)
    
    # Map each letter to a button
    button_letters = {}
    for idx, pin in enumerate(BUTTON_PINS):
        button_letters[pin] = randomizedLetters[idx]
    
    # Set button sequence for the new word
    button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]
    
    # Print new word and letters
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    print("Reallocated letters: " + ' '.join(randomizedLetters))
    print("Available letters: " + ' '.join(randomLetters))
    
    # Reset spelledWord
    spelledWord = ''

# Function to check if button presses match the sequence
def checkSequence():
    global spelledWord, button_sequence
    if len(spelledWord) != len(button_sequence):
        return False
    for i in range(len(spelledWord)):
        if button_sequence[i] != BUTTON_PINS[randomizedLetters.index(spelledWord[i])]:
            return False
    return True

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
randomizedLetters = randomizeLetters(randomWord, randomLetters)

# Map each letter to a button
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    button_letters[pin] = randomizedLetters[idx]

# Set button sequence for the initial word
button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]

# Start the game
print("Welcome to the Word Spelling Game!")
print(f"Spell the word: {randomWord}")
print("Available letters: " + ' '.join(randomLetters))

spelledWord = ''

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
