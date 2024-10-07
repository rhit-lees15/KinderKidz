import argparse
import RPi.GPIO as GPIO 
import vlc
import time
import string
import random
from pygame import Color
from rpi_ws281x import *
import game_sound as gamesound
import finallight as light

# from threading import Thread
# Initialize lights
# LED strip configuration:

### TODO: DisplayManager.py code
LED_COUNT      = 800      # Number of LED pixels.
LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).                                                                                                         PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
###

# GPIO Pins for buttons

### TODO: Button.py
BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]
# Function to generate a random word
# def generateRandomWord(wordList):
    # # Remove the word after chosen
    # word = random.choice(wordList)
    # for word in wordList:
    #     wordList.remove(word)
    # return word
    # return random.choice(wordList)
# Function to generate additional random letters

### TODO: game.py
def generateRandomLetters(remainingLetters, numLetters):
    return random.sample(remainingLetters, numLetters)
# Function to add all letters to one string and shuffle them
def randomizeLetters(word, letters):
    allLetters = list(word + ''.join(letters))
    random.shuffle(allLetters)
    return ''.join(allLetters)

### TODO: DisplayManager.py
def display_letter(letter, color):
    for i in range(len(letter)):
        current_pixel = letter[i]
        strip.setPixelColor(current_pixel, color)
        strip.show() 

def turn_off():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

### TODO: DisplayManager.py ()
def initialize_letter(randomizedLetters):
    current_tile = 0
    for letter in randomizedLetters:
        current_tile += 1
        if current_tile == 1:
            current_letter = light.letter_arrays[letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 2:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 100 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 3:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 200 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 4:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 300 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 5:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 400 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 6:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 500 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 7:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 600 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 8:
            current_letter = light.letter_arrays[letter]
            current_letter = [x + 700 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150)) 

### TODO: DisplayManager.py (This function displays if the input was correct)
def correct_light(letter, pin):
    # might have to map in number to tiles_num by finding which index the pin is located at
    tiles_num = BUTTON_PINS.index(pin)
    addition = tiles_num * 100

    current_letter = light.letter_arrays[letter]
    current_letter = [x + addition for x in current_letter]
    display_letter(current_letter, Color(0, 250,0))


### TODO: DisplayManager.py (This function displays if the input was incorrect)
def wrong_light(letter, pin):
    # might have to map in number to tiles_num by finding which index the pin is located at
    tiles_num = BUTTON_PINS.index(pin)
    addition = tiles_num * 100
    current_letter = light.letter_arrays[letter]
    current_letter = [x + addition for x in current_letter]
    display_letter(current_letter, Color(250, 0,0))

### TODO: Replaces the functions above
def display_output(letter, pin, is_correct):
    # might have to map in number to tiles_num by finding which index the pin is located at
    tiles_num = BUTTON_PINS.index(pin)
    addition = tiles_num * 100
    current_letter = light.letter_arrays[letter]
    current_letter = [x + addition for x in current_letter]
    if (is_correct):
        display_letter(current_letter, Color(0, 250,0))
    else:
        display_letter(current_letter, Color(250, 0,0))

# letters currently do not turn red after getting wrong - next quarter

# Function to handle button press event

### TODO: Button
def buttonPress(pin):
    global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters

    #-----------------------------THREADING ATTEMPT
  
    # if button_is_pressed:
    #     return
    
    # button_is_pressed = 1
    
    # def threaded_function(arg):
    #     for i in range(arg):
    #         print("Button pressed")
    #         time.sleep(1)
    #         button_is_pressed = 0
    #         print("Button is not pressed")
    #         #---------------------- THREADING ATTEMPT
    # spelledWord = ""
    # print("This is running in sound_w_game NOT GUI")

    ### TODO: GameManager.py
    letter = button_letters[pin]
    # time.sleep(0.25)
    if letter in randomWord:
        # Check if the letter is in the correct position
        if letter == randomWord[len(spelledWord)]:
            ## The letter is in the word
            spelledWord += letter
            # print("Current spelling:", spelledWord)
            if len(spelledWord) != len(randomWord):
                ## The letter is in correct position - correct
                #correct_light(pin)
                correct_light(letter, pin)
                gamesound.play_happy()
                gamesound.play_correct_letter()
            # If the full word is spelled correctly
            elif len(spelledWord) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                correct_light(letter, pin)
                gamesound.play_happy()
                turn_off()
                gamesound.play_next_word()
                newWord()
                initialize_letter(randomizedLetters)

        else:
            # Find the first incorrect letter position

            #incorrect_position = spelledWord[]
            # restart_from = randomWord.index(spelledWord[incorrect_position])
            if len(spelledWord) == 0:
                # print("Incorrect order!")
                #spelledWord = ''
                gamesound.play_wrong_order()
                # print("Current spelling:", spelledWord)
            else:
                #spelledWord = randomWord[incorrect_position]
                # print("Incorrect order! Restarting from:", spelledWord)
                gamesound.play_wrong_order()
    else:
        # print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        wrong_light(letter, pin)
        gamesound.play_wrong_letter()
# # Function to handle button press event
# def buttonPress(pin):
#     global spelledWord, randomWord, button_sequence, button_letters
    
#     letter = button_letters[pin]
#     if letter in randomWord:
#         spelledWord += letter
#         print("Current spelling:", spelledWord)
        
#         # Check if the spelled word matches the next letter in the sequence
#         if spelledWord.upper() == randomWord[:len(spelledWord)]:
#             if len(spelledWord) == len(randomWord):
#                 print("Correct! You spelled the word correctly.")
#                 init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
#                 newWord()
#         else:
#             print("Incorrect order! Try again.")
#             init_vlc('./AudioStuff/oopsthatsnotrighttryadifferentorder.mp3')
#             spelledWord = ''
#     else:
#         print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
#         init_vlc('./AudioStuff/nopethatletterisntpartoftheword.mp3')
# Function to generate and display a new word


### TODO: GameManager.py
def newWord():
    global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
    
## NOOR NEW ADDITION 05.09.24
    wordList.remove(randomWord)
    
    if not wordList:
        print("Congratulations! You've spelled all the words in the list!")
        return
    
    
    ################# END OF ADDITION
    # Generate a new word
    n = 0
    while n <= len(wordList) - 1:
        randomWord = wordList[n]
        n += 1
    
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
    # availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
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
    # init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    # print("Reallocated letters: " + ' '.join(randomizedLetters))
    # print("Available letters: " + ' '.join(availableLetters))
    
    # Reset spelledWord
    spelledWord = ''

# --------------------------END OF DEFINITIONS ---------- START OF ACTUAL CALLING

# # Function to check if button presses match the sequence
# def checkSequence():
#     global spelledWord, button_sequence
#     if len(spelledWord) != len(button_sequence):
#         return False
#     for i in range(len(spelledWord)):
#         if button_sequence[i] != BUTTON_PINS[randomizedLetters.index(spelledWord[i])]:
#             return False
#     return True
# Initialize GPIO

### ButtonManager.py
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=1000)
# Generate a random word
# wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
# wordList = ['MY', 'THIS', 'A', 'IS', 'HOME']
# wordList = ['ABC', 'LMNO', 'XYZ']

### TODO: DisplayManager.py
wordDictionary = {
            "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
            "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
            "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
        }
wordList = wordDictionary.get("List 1")
words_remaining = True
random.shuffle(wordList)
# randomWord = generateRandomWord(wordList)
n = 0
while n <= len(wordList) - 1:
    randomWord = wordList[n]
    n += 1
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


### TODO: main.py
if __name__ == '__main__':
    #####* Start the game
    # Initialization of lights    
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    # Create NeoPixel object with appropriate configuration.
    ### TODO: DisplayManager.py
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    # #-------------------------------------THREADING ATTEMPT
    # thread = Tread(target = threaded_function, args = (10, ))
    # thread.start()
    # tread.join()
    # print("Thread finished.....exiting")
    # #--------------------------------------------THREADING

    ### TODO: game.py
    print("Welcome to the Word Spelling Game!")
    gamesound.play_intro()
    print(f"Spell the word: {randomWord}")
    # print("Reallocated letters: " + ' '.join(randomizedLetters))
    # print("Available letters: " + ' '.join(availableLetters))
    spelledWord = ''
    initialize_letter(randomizedLetters)
    try:
        while words_remaining:
            if not wordList:
                words_remaining = False
                
            time.sleep(0.25)
        else:
             turn_off()

            
    except KeyboardInterrupt:
        turn_off()
        GPIO.cleanup()