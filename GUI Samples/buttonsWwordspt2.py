import RPi.GPIO as GPIO
import string
import random
import time

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Function to generate a random word
def generateRandomWord(words):
    return random.choice(words)

# Function to handle button press event
def buttonPress(pin):
    global spelledWord, randomWord
    
    letter = button_letters[pin]
    
    if len(spelledWord) < len(randomWord) and letter == randomWord[len(spelledWord)]:
        spelledWord += letter
        print("Current spelling:", spelledWord)
        if spelledWord == randomWord:
            print("Correct! You spelled the word correctly.")
            newWord()
    else:
        print(f"Incorrect! Button {pin} (Letter {letter}) pressed at the wrong position.")

# Function to generate and display a new word
def newWord():
    global spelledWord, randomWord
    randomWord = generateRandomWord(wordList)
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    spelledWord = ''

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=200)

# Generate a random word
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(wordList)

# Map each letter to a button
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    if idx < len(randomWord):
        button_letters[pin] = randomWord[idx]

# Start the game
print("Welcome to the Word Spelling Game!")
print(f"Spell the word: {randomWord}")

spelledWord = ''

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
