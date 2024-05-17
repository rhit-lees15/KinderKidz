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

import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from tkinter.messagebox import showinfo
import sound_w_gamecopy as game_sequence
import game_sound as gamesound 

# Initialize lights
# LED strip configuration:
LED_COUNT      = 800      # Number of LED pixels.
LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).                                                                                                         PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 15     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# GPIO Pins for buttons
BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]

# time per lesson (3 min = 180)
duration = 30

# Function to generate additional random letters
def generateRandomLetters(remainingLetters, numLetters):
    return random.sample(remainingLetters, numLetters)

# Function to add all letters to one string and shuffle them
def randomizeLetters(word, letters):
    allLetters = list(word + ''.join(letters))
    random.shuffle(allLetters)
    return ''.join(allLetters)

def display_letter(letter, color):
    for i in range(len(letter)):
        current_pixel = letter[i]
        strip.setPixelColor(current_pixel, color)
        strip.show() 

def turn_off():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

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

def correct_light(letter, pin):
    # might have to map in number to tiles_num by finding which index the pin is located at
    tiles_num = BUTTON_PINS.index(pin)
    addition = tiles_num * 100
    current_letter = light.letter_arrays[letter]
    current_letter = [x + addition for x in current_letter]
    display_letter(current_letter, Color(0, 250,0))

# letters currently do not turn red after getting wrong - next quarter
def wrong_light(letter, tiles_num):
    addition = (tiles_num - 1) * 100
    current_letter = light.letter_arrays[letter]
    current_letter = [x + addition for x in current_letter]
    display_letter(current_letter, Color(250, 0, 0))


# Function to handle button press event
def buttonPress(pin):
    global spelled_word, randomWord, randomizedLetters, button_sequence, button_letters

    letter = button_letters[pin]
    if letter in randomWord:
        # Check if the letter is in the correct position
        if letter == randomWord[len(spelled_word)]:
            ## The letter is in the word
            spelled_word += letter
            print("Current spelling:", spelled_word)
            if len(spelled_word) != len(randomWord):
                ## The letter is in correct position - correct
                correct_light(letter, pin)
                gamesound.play_happy()
                gamesound.play_correct_letter()
            # If the full word is spelled correctly
            elif len(spelled_word) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                correct_light(letter, pin)
                gamesound.play_happy()
                turn_off()
                gamesound.play_next_word()
                newWord()
                initialize_letter(randomizedLetters)

        else:
            # Find the first incorrect letter position
            if len(spelled_word) == 0:
                print("Incorrect order!")
                #spelled_word = ''
                gamesound.play_wrong_order()
                print("Current spelling:", spelled_word)
            else:
                #spelled_word = randomWord[incorrect_position]
                print("Incorrect order! Restarting from:", spelled_word)
                gamesound.play_wrong_order()
    else:
        print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        gamesound.play_wrong_letter()

# Function to generate and display a new word
def newWord():
    global spelled_word, randomWord, randomizedLetters, button_sequence, button_letters
    
    wordList.remove(randomWord)
    
    if not wordList:
        print("Congratulations! You've spelled all the words in the list!")
        return

    # Generate a new word
    n = 0
    while n <= len(wordList) - 1:
        randomWord = wordList[n]
        n += 1
    
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(spelled_word) - set(randomWord))

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
    
    # Reset spelled_word
    spelled_word = ''

# Initialize GPIO
# GPIO.setmode(GPIO.BCM)
# for pin in BUTTON_PINS:
#     GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=1000)

# Generate a random word
wordDictionary = {
            "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
            "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
            "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
        }

# wordList = wordDictionary.get(word_list_name)

# words_remaining = True

# random.shuffle(wordList)
# # randomWord = generateRandomWord(wordList)
# n = 0
# while n <= len(wordList) - 1:
#     randomWord = wordList[n]
#     n += 1

# # Get remaining letters
# availableLetters = list(set(string.ascii_uppercase) - set(randomWord))

# # Generate additional random letters
# randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))

# # Combine the random word and random letters into a single string and shuffle them
# randomizedLetters = randomizeLetters(randomWord, randomLetters)

# # Map each letter to a button
# button_letters = {}
# for idx, pin in enumerate(BUTTON_PINS):
#     button_letters[pin] = randomizedLetters[idx]

# # Set button sequence for the initial word
# button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]

#--------------------------------------------------------------------

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive GUI")
        self.attributes('-fullscreen', True)  # Make the GUI full screen

        self.current_page = None
        self.pages = {}  # Dictionary to store pages

        # Define your word lists
        self.word_lists = {
            "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
            "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
            "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
        }
        spelled_word = ""
        self.create_start_page()

    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self, bg = 'black')
        start_page.pack(fill=tk.BOTH, expand=True)

        # Central Picture 
        image_path = "./Images/ANIMALS.png" # ./Images/name.type
        image = self.load_image(image_path)
        picture_label = tk.Label(start_page, image=image, borderwidth=0)
        picture_label.image = image
        picture_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Start button
        start_button = tk.Button(start_page, text="Start", bg="green", font=("Helvetica", 40),
                                 command=self.create_list_selection_page)
        start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(start_page, text="Exit", bg="red", font=("Helvetica", 20),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["start"] = start_page  # Store the start page

    def load_image(self, path):
        image = tk.PhotoImage(file=path)
        return image

    def create_list_selection_page(self):
        self.hide_current_page()  # Hide current page
        
        gamesound.play_intro()

        # spelled_word = ''

        self.current_page = "list_selection"
        list_selection_page = tk.Frame(self, bg="black")
        list_selection_page.pack(fill=tk.BOTH, expand=True)

        gamesound.play_choose_list()

        # Label for word list selection
        list_label = tk.Label(list_selection_page, text="Select a Word List:", font=("Helvetica", 20), bg="black", fg="white")
        list_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Button to select first word list
        first_list_button = tk.Button(list_selection_page, text="List 1", font=("Helvetica", 40),
                                    bg="blue", fg="white", command=lambda: self.create_word_display_page("List 1"))
        first_list_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        # Button to select second word list
        second_list_button = tk.Button(list_selection_page, text="List 2", font=("Helvetica", 40),
                                    bg="green", fg="white", command=lambda: self.create_word_display_page("List 2"))
        second_list_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Button to select third word list
        third_list_button = tk.Button(list_selection_page, text="List 3", font=("Helvetica", 40),
                                    bg="red", fg="white", command=lambda: self.create_word_display_page("List 3"))
        third_list_button.place(relx=0.8, rely=0.5, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(list_selection_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

        self.pages["list_selection"] = list_selection_page  # Store the time selection page

#_----------------------------
    def create_word_display_page(self, word_list_name):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"

        print('Before ButtonPress')

        # Generate a new random word from the selected word list
        self.selected_word_list = self.word_lists.get(word_list_name)
        self.my_new_word()

        GPIO.setmode(GPIO.BCM)
        for pin in BUTTON_PINS:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin, self.randomWord, spelled_word), bouncetime=3000)

        def buttonPress(self, pin, randomWord, spelled_word):
            global button_sequence, button_letters

            letter = button_letters[pin]
            time.sleep(0.25)
            if letter in randomWord:
                # Check if the letter is in the correct position
                if letter == randomWord[len(spelled_word)]:
                    ## The letter is in the word
                    spelled_word += letter
                    print("Current spelling:", spelled_word)
                    if len(spelled_word) != len(randomWord):
                        ## The letter is in correct position - correct
                        gamesound.play_happy()
                        gamesound.play_correct_letter()
                    # If the full word is spelled correctly
                    elif len(spelled_word) == len(randomWord):
                        print("Correct! You spelled the word correctly.")
                        gamesound.play_happy()
                        gamesound.play_next_word()
                        game_sequence.newWord()
                else:
                    # Find the first incorrect letter position
                    if len(spelled_word) == 0:
                        print("Incorrect order!")
                        #spelled_word = ''
                        gamesound.play_wrong_order()
                        print("Current spelling:", spelled_word)
                    else:
                        #spelled_word = randomWord[incorrect_position]
                        print("Incorrect order! Restarting from:", spelled_word)
                        gamesound.play_wrong_order()
            else:
                print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
                gamesound.play_wrong_letter()

    def my_new_word(self):
        self.words_remaining = True
        self.randomWord = random.choice(self.selected_word_list)

        # Get remaining letters
        availableLetters = list(set(string.ascii_uppercase) - set(self.randomWord))

        # Generate additional random letters
        randomLetters = game_sequence.generateRandomLetters(availableLetters, 8 - len(self.randomWord))

        # Combine the random word and random letters into a single string and shuffle them
        randomizedLetters = game_sequence.randomizeLetters(self.randomWord, randomLetters)

        # Map each letter to a button
        for idx, pin in enumerate(game_sequence.BUTTON_PINS):
            self.button_letters[pin] = randomizedLetters[idx]

        # Set button sequence for the initial word
        self.button_sequence = [game_sequence.BUTTON_PINS[randomizedLetters.index(letter)] for letter in self.randomWord]

        try:
            while words_remaining:
                if not self.word_list_name:
                    words_remaining = False
                  
                time.sleep(0.25)

        except KeyboardInterrupt:
            GPIO.cleanup()

        # Display word
        word_display_page = tk.Frame(self, bg="black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=self.randomWord, font=("Helvetica", 48),
                            bg="black", fg="white")
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["word_display"] = word_display_page  # Store the word display page
    
    def create_word_display_page(self, word_list_name):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"
        
        randomWord = random.choice(self.word_lists[word_list_name])

        # Display word
        word_display_page = tk.Frame(self, bg = "black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=randomWord, font=("Helvetica", 48),
                             bg = "black", fg = "white")
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["word_display"] = word_display_page  # Store the word display page

    def create_countdown(self, frame, duration):
        countdown_label = tk.Label(frame, font=("Helvetica", 16))
        countdown_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

        def update_countdown(duration):    
        
            min, sec = divmod(duration,60)
            countdown_label.config(text=f"Time Left: {min}:{sec}", bg = "black", fg = "white")


            if duration > 0:
                frame.after(1000, update_countdown, duration - 1)
            else:
                self.create_dance_display_page()

        update_countdown(duration)

    # Function to switch back to word display after the song finishes
    def back_to_word_display(word_list_name):
        # Destroy the dance display page
        app.pages["dance_display"].destroy()
        # Re-create the word display page
        app.create_word_display_page(word_list_name)
        pass
#_----------------------------
    def create_dance_display_page(self):
        # gamesound.play_dance_break()
        self.hide_current_page()  # Hide current page
        self.current_page = "Dance_display"
        dance_display_page = tk.Frame(self, bg="black")
        dance_display_page.pack(fill=tk.BOTH, expand=True)

        # gamesound.play_dance_break()

        # Label for word list selection -- this does not show up, and unsure as to why
        dance_label = tk.Label(dance_display_page, text="Select a Song:", font=("Helvetica", 20), bg="black", fg="white")
        dance_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        gamesound.play_dance_break()

       # Button for songs
        audio_button_1 = tk.Button(dance_display_page, text="Puff the Magic Dragon", font=("Helvetica", 20),
                                    bg="blue", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/puff-the-magic-dragon.mp3"))
        audio_button_1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        audio_button_2 = tk.Button(dance_display_page, text="Twinkle, Twinkle", font=("Helvetica", 20),
                                    bg="red", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/twinkle-twinkle.mp3"))
        audio_button_2.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        audio_button_3 = tk.Button(dance_display_page, text="My Year - ZOMBIES", font=("Helvetica", 20),
                                    bg="orange", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/my-year-zombies.mp3"))
        audio_button_3.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

        audio_button_4 = tk.Button(dance_display_page, text="If You're Happy and You Know It", font=("Helvetica", 20),
                                    bg="purple", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/happy-and-you-know-it.mp3"))
        audio_button_4.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        audio_button_5 = tk.Button(dance_display_page, text="Body Bop Bop", font=("Helvetica", 20),
                                    bg="green", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/body-bop-bop.mp3"))
        audio_button_5.place(relx=0.7, rely=0.6, anchor=tk.CENTER)

        # Exit button
        restart_button = tk.Button(dance_display_page, text="List Selection", bg="green", font=("Helvetica", 16),
                                command=self.create_list_selection_page)
        restart_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["dance_display"] = dance_display_page  # Store the data

    def create_dance_image_page(self):
        self.current_page = "dance image"
        image_page = tk.Frame(self, bg = 'black')
        image_page.pack(fill=tk.BOTH, expand=True)

        # Central Picture 
        image_path_2 = "./Images/COW.PNG" # ./Images/name.type
        image_2 = self.load_image(image_path_2)
        picture_label_2 = tk.Label(image_page, image=image_2, borderwidth=0)
        picture_label_2.image = image_2
        picture_label_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Start button
        start_button = tk.Button(image_page, text="Start", bg="green", font=("Helvetica", 40))
        start_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(image_page, text="Exit", bg="red", font=("Helvetica", 20))
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["start"] = image_page  # Store the start page

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

#--------------------------------------------------------------------


if __name__ == '__main__':
    
    app = GUI()   
    app.mainloop()
    
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
    gamesound.play_intro()
    print(f"Spell the word: {randomWord}")
    print("Reallocated letters: " + ' '.join(randomizedLetters))

    spelled_word = ''

    initialize_letter(randomizedLetters)

    try:
        while words_remaining:
            if not wordList:
                words_remaining = False
                
            time.sleep(0.25)
            

    except KeyboardInterrupt:
        GPIO.cleanup()
