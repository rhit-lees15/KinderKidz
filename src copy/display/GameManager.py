import random
import time
import RPi.GPIO as GPIO
import string
# from display.Button import Button

# from display.Button import Button
# from display.config import 
from display.DisplayManager import DisplayManager
# from Button import Button
from display.MyGUI import GUI
from display.GameSound import Audio

class Game:
    # Dictionary of all the words included in the spelling game
    word_list = ['MY', 'THIS', 'A', 'IS', 'HOME','THE', 'IN', 'CITY', 'BY', 'OCEAN','ON', 'NOT', 'FARM', 'LIKE', 'I']
    BUTTON_PINS = [24, 25, 23, 22, 5, 6, 13, 12]  
      
    GPIO.setmode(GPIO.BCM)
    for pin in BUTTON_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: DisplayManager.buttonPress(pin), bouncetime=1000)
    
    words_remaining = True
    random.shuffle(word_list)
    DisplayManager.newWord()
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
        
