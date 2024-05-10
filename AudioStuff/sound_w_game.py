
import argparse
import RPi.GPIO as GPIO 
import vlc
import time
import string
import random
from pygame import Color
from rpi_ws281x import *

# from game_sound import *




# def init_vlc(song:str):
#     vlc_instance = vlc.Instance()
#     player = vlc_instance.media_player_new()

#     media  = vlc_instance.media_new(song)
#     media.get_mrl()
#     player.set_media(media)
#     player.play()
#     # playing = set(State.playing)
#     time.sleep(1.5) # startup time.
#     duration = player.get_length() / 1000
#     mm, ss   = divmod(duration, 60)

def init_vlc(sound_file:str):
    p = vlc.MediaPlayer(sound_file)
    p.play()
    time.sleep(1) #this is necessary because is_playing() returns false if called right away
    while p.is_playing():
        time.sleep(0.25)
    p.release()

# Initialize lights
# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 65     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

    

    

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Function to generate a random word
# def generateRandomWord(wordList):
#     # # Remove the word after chosen
#     # word = random.choice(wordList)
#     # for word in wordList:
#     #     wordList.remove(word)
#     # return word
#     return random.choice(wordList)

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
    time.sleep(0.25)
    if letter in randomWord:
        # Check if the letter is in the correct position
        if letter == randomWord[len(spelledWord)]:
            ## The letter is in the word
            spelledWord += letter
            print("Current spelling:", spelledWord)
            if len(spelledWord) != len(randomWord):
                ## The letter is in correct position - correct
                init_vlc('./AudioStuff/goodjobnowletsfindthenextletter.mp3')
            # If the full word is spelled correctly
            elif len(spelledWord) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
                newWord()
        else:
            # Find the first incorrect letter position
            #incorrect_position = spelledWord[]
            # restart_from = randomWord.index(spelledWord[incorrect_position])
            if len(spelledWord) == 0:
                print("Incorrect order!")
                #spelledWord = ''
                init_vlc('./AudioStuff/oopsthatsnotrighttryadifferentorder.mp3')
                print("Current spelling:", spelledWord)
            else:
                #spelledWord = randomWord[incorrect_position]
                print("Incorrect order! Restarting from:", spelledWord)
                init_vlc('./AudioStuff/oopsthatsnotrighttryadifferentorder.mp3')
    else:
        print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        init_vlc('./AudioStuff/nopethatletterisntpartoftheword.mp3')


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
    print("Reallocated letters: " + ' '.join(randomizedLetters))
    # print("Available letters: " + ' '.join(availableLetters))
    
    # Reset spelledWord
    spelledWord = ''

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
GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=200)

# Generate a random word
# wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
# wordList = ['MY', 'THIS', 'A', 'IS', 'HOME']
wordList = ['ABC', 'LMNO', 'XYZ']

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

if __name__ == '__main__':
    #####* Start the game

    # Initialization of lights    
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()


    print("Welcome to the Word Spelling Game!")
    init_vlc('./AudioStuff/hicarmineletsspellsomewordstoday.mp3')
    print(f"Spell the word: {randomWord}")
    print("Reallocated letters: " + ' '.join(randomizedLetters))
    # print("Available letters: " + ' '.join(availableLetters))

    spelledWord = ''

    try:
        while words_remaining:
            if not wordList:
                words_remaining = False
                
            time.sleep(0.25)
            

    except KeyboardInterrupt:
        GPIO.cleanup()


# GPIO.cleanup() # Clean up

# names of audio files for convenience

# firstletsfindtheletterC.mp3
# ByeCarmine.mp3 
# goodjobnowletsfindthenextletter.mp3 
# GreatworkCarmine.mp3 
# hicarmineletsspellsomewordstoday.mp3 
# letsfindtheletterT.mp3 
# pressthegreenbuttontostart.mp3 
# repeataftermeispelledthewordcatcatisspelledCAT.mp3 
# thetimerranoutletshaveadancebreak.mp3 
# timetomoveontothenextword.mp3 
# werespellingthewordcatcatisspelledCAT.mp3 
# whereistheletterA_.mp3 
# youspelledthewordcatcatisspelledCAT.mp3
# nopethatletterisntpartoftheword.mp3
# oopsthatsnotrighttryadifferentorder.mp3