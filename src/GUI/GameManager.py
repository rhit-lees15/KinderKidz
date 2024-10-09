import random
import time
import RPi.GPIO as GPIO
import string
from display.Button import Button

from display.Button import Button
# from display.config import 
from display.DisplayManager import DisplayManager
from GUI.MyGUI import GUI
from Media.GameSound import Audio

class Game:
    
    GPIO.setmode(GPIO.BCM)
    for pin in BUTTON_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=1000)

    # Dictionary of all the words included in the spelling game
    word_list = ['MY', 'THIS', 'A', 'IS', 'HOME','THE', 'IN', 'CITY', 'BY', 'OCEAN','ON', 'NOT', 'FARM', 'LIKE', 'I']
    BUTTON_PINS = [24, 25, 23, 22, 5, 6, 13, 12]
    
    words_remaining = True
    random.shuffle(word_list)
    
    n = 0
    while n <= len(word_list) - 1:
        randomWord = word_list[n]
        n += 1
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
    # Generate additional random letters
    randomLetters = Button.generateRandomLetters(availableLetters, 8 - len(randomWord))
    # Combine the random word and random letters into a single string and shuffle them
    randomizedLetters = Button.randomizeLetters(randomWord, randomLetters)
    # Map each letter to a button
    button_letters = {}
    for idx, pin in enumerate(BUTTON_PINS):
        button_letters[pin] = randomizedLetters[idx]
    # Set button sequence for the initial word
    button_sequence = [BUTTON_PINS[Button.randomizedLetters.index(letter)] for letter in randomWord]
        
    GUI.__init__()
    Audio.play_intro()
    GUI.create_start_page()
    
    GUI.create_time_selection_page()
    GUI.create_word_display_page()
    GUI.create_countdown()
    
    # Function to create a list of additional letters to include, dependent on the length of the word
    def gen_random_letters(remainingLetters, numLetters):
        return random.sample(remainingLetters, numLetters)
    
    # Function to add all letters to one string and shuffle them
    def randomize_Letters(word, letters):
        allLetters = list(word + ''.join(letters))
        random.shuffle(allLetters)
        return ''.join(allLetters)

    DisplayManager.display_letter()
    DisplayManager.turn_off()
    DisplayManager.initialize_letter()
    DisplayManager.correct_light()
    DisplayManager.wrong_light()
    
    GUI.create_dance_display_page()
    GUI.back_to_word_display()
        
