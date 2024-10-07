import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from tkinter.messagebox import showinfo
import random
# import sound_w_game as game_sequence
# import game_sound as gamesound
import time
# import vlc
import string
# import RPi.GPIO as GPIO 
# from pygame import Color
# from rpi_ws281x import *

# BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]

# import pygame.mixer

# pygame.mixer.init()

# time per lesson (3 min = 180)
duration = 30

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

        self.create_start_page()

    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self, bg = 'black')
        start_page.pack(fill=tk.BOTH, expand=True)

        # Central Picture 
        image_path = "./Media/Images/ANIMALS.png" # ./Images/name.type
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

        # gamesound.play_choose_list()

    def load_image(self, path):
        image = tk.PhotoImage(file=path)
        return image

    def create_list_selection_page(self):
        self.hide_current_page()  # Hide current page
        
        # gamesound.play_intro()

        # spelledWord = ''

        self.current_page = "list_selection"
        list_selection_page = tk.Frame(self, bg="black")
        list_selection_page.pack(fill=tk.BOTH, expand=True)

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
        

    def create_word_display_page(self, word_list_name):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"
        
        # Generate a new random word
        # newWord()

        # Get the random word
        # randomWord = spelledWord

        # print('Before ButtonPress')

        # Generate a new random word from the selected word list
        randomWord = random.choice(self.word_lists.get(word_list_name))

        # randomWord = random.choice(self.word_lists[word_list_name])

#############################

        # GPIO.setmode(GPIO.BCM)
        # for pin in BUTTON_PINS:
        #     GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #     GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin, randomWord), bouncetime=3000)

        # randomLetters = game_sequence.generateRandomLetters(availableLetters, 8 - len(randomWord))
        # randomizedLetters = game_sequence.randomizeLetters(randomWord, randomLetters)
        # game_sequence.generateRandomLetters()
        # game_sequence.randomizeLetters()
        # game_sequence.buttonPress(pin, randomWord)
        # def buttonPress(pin, randomWord):
        #     global spelledWord, button_sequence, button_letters
            
        #     spelledWord = ""

        #     letter = button_letters[pin]
        #     time.sleep(0.25)
        #     if letter in randomWord:
        #         # Check if the letter is in the correct position
        #         if letter == randomWord[len(spelledWord)]:
        #             ## The letter is in the word
        #             spelledWord += letter
        #             print("Current spelling:", spelledWord)
        #             if len(spelledWord) != len(randomWord):
        #                 ## The letter is in correct position - correct
        #                 gamesound.play_happy()
        #                 gamesound.play_correct_letter()
        #             # If the full word is spelled correctly
        #             elif len(spelledWord) == len(randomWord):
        #                 print("Correct! You spelled the word correctly.")
        #                 gamesound.play_happy()
        #                 gamesound.play_next_word()
        #                 newWord()
        #         else:
        #             # Find the first incorrect letter position
        #             #incorrect_position = spelledWord[]
        #             # restart_from = randomWord.index(spelledWord[incorrect_position])
        #             if len(spelledWord) == 0:
        #                 print("Incorrect order!")
        #                 #spelledWord = ''
        #                 gamesound.play_wrong_order()
        #                 print("Current spelling:", spelledWord)
        #             else:
        #                 #spelledWord = randomWord[incorrect_position]
        #                 print("Incorrect order! Restarting from:", spelledWord)
        #                 gamesound.play_wrong_order()
        #     else:
        #         print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        #         gamesound.play_wrong_letter()
        # game_sequence.newWord()

        # words_remaining = True

        # random.shuffle(word_list_name)
        # randomWord = generateRandomWord(wordList)
        # n = 0
        # while n <= len(word_list_name) - 1:
        #     randomWord = word_list_name[n]
        #     n += 1

        # # Get remaining letters
        # availableLetters = list(set(string.ascii_uppercase) - set(randomWord))

        # # Generate additional random letters
        # randomLetters = game_sequence.generateRandomLetters(availableLetters, 8 - len(randomWord))

        # # Combine the random word and random letters into a single string and shuffle them
        # randomizedLetters = game_sequence.randomizeLetters(randomWord, randomLetters)

        # # Map each letter to a button
        # button_letters = {}
        # for idx, pin in enumerate(game_sequence.BUTTON_PINS):
        #     button_letters[pin] = randomizedLetters[idx]

        # # Set button sequence for the initial word
        # button_sequence = [game_sequence.BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]

        # # spelledWord = ''


    # if __name__ == '__main__':
    #     gamesound.play_intro()
    #     spelledWord = ''


        try:
            while words_remaining:
                if not word_list_name:
                    words_remaining = False
                  
                time.sleep(0.25)

        except KeyboardInterrupt:
            GPIO.cleanup()

#################################


        # Display word
        word_display_page = tk.Frame(self, bg="black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=randomWord, font=("Helvetica", 48),
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

        # Random word generator -- used for initial testing
        # word_list = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
        
        randomWord = random.choice(self.word_lists[word_list_name])

        # Display word
        word_display_page = tk.Frame(self, bg = "black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=randomWord, font=("Helvetica", 48),
                             bg = "black", fg = "white")
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        ## This is too much of a distraction, so we removed it
        # # Change color of each word
        # colors = ["red", "blue", "green", "purple", "orange"]  # List of colors
        # for i, letter in enumerate(randomWord):
        #     color = random.choice(colors)  # Pick a random color
        #     word_text.config(fg=color)
        #     word_text.update_idletasks()
        #     word_text.after(1000 * i, lambda: None)  # Delay for each letter


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
                # gamesound.play_dance_break()

        update_countdown(duration)

    # Function to switch back to word display after the song finishes
    def back_to_word_display(word_list_name):
        # Destroy the dance display page
        app.pages["dance_display"].destroy()
        # Re-create the word display page
        app.create_word_display_page(word_list_name)
        pass

    # def play_selected_song(selected_song):
    #     if word_list_name =
    #         './AudioStuff/hicarmineletsspellsomewordstoday.mp3'
    #     gamesound.init_vlc(selected_song)
        # pygame.mixer.music.load(selected_song)
        # pygame.mixer.music.play()
        # # Calculate the duration of the song and call a function to switch back to word display after the duration
        # song_duration = pygame.mixer.Sound(selected_song).get_length()
        # root.after((song_duration * 1000), back_to_word_display)

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

        # gamesound.play_dance_break()
########################

       # Button for songs
        # audio_button_1 = tk.Button(dance_display_page, text="Puff the Magic Dragon", font=("Helvetica", 20),
        #                             bg="blue", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/puff-the-magic-dragon.mp3"))
        # audio_button_1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        # audio_button_2 = tk.Button(dance_display_page, text="Twinkle, Twinkle", font=("Helvetica", 20),
        #                             bg="red", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/twinkle-twinkle.mp3"))
        # audio_button_2.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        # audio_button_3 = tk.Button(dance_display_page, text="My Year - ZOMBIES", font=("Helvetica", 20),
        #                             bg="orange", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/my-year-zombies.mp3"))
        # audio_button_3.place(relx=0.3, rely=0.6, anchor=tk.CENTER)

        # audio_button_4 = tk.Button(dance_display_page, text="If You're Happy and You Know It", font=("Helvetica", 20),
        #                             bg="purple", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/happy-and-you-know-it.mp3"))
        # audio_button_4.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # audio_button_5 = tk.Button(dance_display_page, text="Body Bop Bop", font=("Helvetica", 20),
        #                             bg="green", fg="white", command=lambda: gamesound.init_vlc("./AudioStuff/body-bop-bop.mp3"))
        # audio_button_5.place(relx=0.7, rely=0.6, anchor=tk.CENTER)


        audio_button_1 = tk.Button(dance_display_page, text="Puff the Magic Dragon", font=("Helvetica", 20),
                                    bg="blue", fg="white")
        audio_button_1.place(relx=0.3, rely=0.4, anchor=tk.CENTER)


#####################



        # # Create a Listbox
        # songs = ('Song 1', 'Song 2', 'Song 3', 'Song 4')
        
        # listbox = tk.Listbox(dance_display_page, height=6, selectmode=tk.EXTENDED, bg="black", fg="white", font=("Helvetica", 24))
        # listbox.pack(side=tk.LEFT, padx=0, pady=20, fill=tk.BOTH, expand=True)

        # # for song in songs:
        # #     listbox.insert(tk.END, song)

        # # Link a scrollbar to the Listbox
        # # scrollbar = ttk.Scrollbar(dance_display_page, orient=tk.VERTICAL, command=listbox.yview)
        # # scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        # # listbox.config(yscrollcommand=scrollbar.set)

        # # Function to handle song selection
        # def play_song():
        #     selected_song_index = listbox.curselection()
        #     if selected_song_index:
        #         selected_song = songs[selected_song_index[0]]  # Get the selected song
        #         play_selected_song(selected_song)

        # # Button to play the selected song
        # play_button = tk.Button(dance_display_page, text="Play", bg="green", font=("Helvetica", 16), command=play_song)
        # play_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Exit button
        restart_button = tk.Button(dance_display_page, text="List Selection", bg="green", font=("Helvetica", 16),
                                command=self.create_list_selection_page)
        restart_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["dance_display"] = dance_display_page  # Store the data

################# IMAGE ATTEMPT
    def create_dance_image_page(self):
        self.current_page = "dance image"
        image_page = tk.Frame(self, bg = 'black')
        image_page.pack(fill=tk.BOTH, expand=True)

        # Central Picture 
        image_path_2 = "./Media/Images/COW.PNG" # ./Images/name.type
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

################### IMAGE ADD

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()   
    app.mainloop()