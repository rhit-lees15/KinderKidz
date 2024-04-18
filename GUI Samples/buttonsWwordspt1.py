# import RPi.GPIO as GPIO
import time
import string
import random

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Function to generate a random word
def generateRandomWord(words):
    return random.choice(words)

# Generate a random word
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(wordList)

print('Spell the word: ', randomWord)

# Function to remove letters from the alphabet
def removeLetters(letters2Remove):
    alphabet = list(string.ascii_uppercase)
    
    for letter in letters2Remove:
        if letter in alphabet:
            alphabet.remove(letter)
    alphabetString = ''.join(alphabet)
    return alphabetString

# Get remaining letters
letters2Remove = randomWord
availableLetters = removeLetters(letters2Remove)

# Function to generate additional random letters
def generateRandomLetters(remainingLetters):
    chosenLetters = random.sample(availableLetters, remainingLetters)
    return ''.join(chosenLetters)
    
# Generate additional random letters
remainingLetters = 8 - len(randomWord)
randomLetters = generateRandomLetters(remainingLetters)

# Function to add all letters to one string
def randomizeLetters(word, letters):
    allLetters = list(word + letters)
    random.shuffle(allLetters)
    return ''.join(allLetters)

# Final randomized letter sequence
randomizedLetters = randomizeLetters(randomWord, randomLetters)

print('Buttons will have the following letters:', randomizedLetters)

# Map button pins to random letters
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    button_letters[pin] = randomizedLetters[idx]

# Set up GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        for pin in BUTTON_PINS:
            if GPIO.input(pin) == GPIO.LOW:
                if pin in button_letters:
                    print(f"Button {pin} (Letter {button_letters[pin]}) is pressed - {'correct' if button_letters[pin] == randomizedLetters[0] else 'incorrect'}")
                    # Remove the pressed letter from the randomizedLetters sequence
                    randomizedLetters = randomizedLetters[1:]
                else:
                    print(f"Button {pin} is pressed but not assigned a letter.")
            else:
                pass
            print(f"Button {pin} (Letter {button_letters[pin]})")
        time.sleep(0.5)
        
except KeyboardInterrupt:
    GPIO.cleanup()

# for pin in BUTTON_PINS:
#     print(f"Button {pin} (Letter {button_letters[pin]})")