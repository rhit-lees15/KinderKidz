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
    global spelledWord, randomWord, button_sequence, button_letters
    
    letter = button_letters[pin]
    if letter in randomWord:
        # Check if the letter is in the correct position
        if spelledWord + letter == randomWord[:len(spelledWord) + 1]:
            spelledWord += letter
            print("Current spelling:", spelledWord)
            
            # If the full word is spelled correctly
            if len(spelledWord) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                newWord()
        else:
            # Find the first incorrect letter position
            incorrect_position = len(spelledWord)
            restart_from = randomWord.index(spelledWord[incorrect_position])
            spelledWord = randomWord[restart_from]
            print("Incorrect order! Restarting from:", spelledWord)
    else:
        print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")

# Function to generate and display a new word
def newWord():
    global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
    
    # Generate a new word
    randomWord = generateRandomWord(wordList)
    
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
    
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
    
    # Reset spelledWord
    spelledWord = ''

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
print("Reallocated letters: " + ' '.join(randomizedLetters))

spelledWord = ''

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
