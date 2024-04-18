import RPi.GPIO as GPIO
import string
import random
import time

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Function to generate a random word
def generateRandomWord(words):
    return random.choice(words)

# Function to remove letters from the alphabet
def removeLetters(word):
    alphabet = list(string.ascii_uppercase)
    
    for letter in word:
        if letter in alphabet:
            alphabet.remove(letter)
    return alphabet

# Function to generate additional random letters
def generateRandomLetters(remainingLetters):
    return random.sample(remainingLetters, 8 - len(randomWord))

# Function to add all letters to one string
def randomizeLetters(word, letters):
    allLetters = list(word + ''.join(letters))
    random.shuffle(allLetters)
    return ''.join(allLetters)

# Function to handle button press event
def buttonPress(pin):
    global randomizedLetters, currentWordIndex
    
    letter = button_letters[pin]
    if letter == randomizedLetters[currentWordIndex]:
        print(f"Button {pin} (Letter {letter}) is pressed - Correct!")
        currentWordIndex += 1
        if currentWordIndex == len(randomizedLetters):
            newWord()
    else:
        print(f"Button {pin} (Letter {letter}) is pressed - Incorrect!")

# Function to generate and display a new word
def newWord():
    global randomizedLetters, currentWordIndex
    randomWord = generateRandomWord(wordList)
    availableLetters = removeLetters(randomWord)
    remainingLetters = generateRandomLetters(availableLetters)
    randomizedLetters = randomizeLetters(randomWord, remainingLetters)
    currentWordIndex = 0
    print(f"Spell the word: {randomWord}")

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=200)

# Generate a random word
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(wordList)

print('The randomword is: ', randomWord)

# Get remaining letters
availableLetters = removeLetters(randomWord)

# Generate additional random letters
remainingLetters = generateRandomLetters(availableLetters)

# Final randomized letter sequence
randomizedLetters = randomizeLetters(randomWord, remainingLetters)

print('Randomized Letters: ', randomizedLetters)

# Map button pins to random letters
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    button_letters[pin] = randomizedLetters[idx]

# Start the game
currentWordIndex = 0
newWord()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
