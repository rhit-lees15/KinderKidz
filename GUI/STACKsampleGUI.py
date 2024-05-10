#### NEED TO MAKE THE PAGES NOT STACK ON ONE ANOTHER
### ALSO PICS DON'T WORK ON THIS ONE & NO FULL SCREEN

import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import time
from PIL import Image, ImageTk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # self.geometry("800x800")
        self.title("Interactive GUI")

        self.current_page = None
        self.create_start_page()

        # Start page w/ exit button
    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self)
        start_page.pack(fill=tk.BOTH, expand=True)

        # Start button
        start_button = tk.Button(start_page, text="Start", bg="green", font=("Helvetica", 16),
                                 command=self.create_time_selection_page)
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(start_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        # Displaying images in the four corners
        # Could make this into a loop instead of individual??
        #         def display_corner_images(self, parent_frame):
        # """Display images in the four corners of the parent frame."""
        # images = ["Chase.jpg", "Marshall.jpg", "Rubble.jpg", "Zuma.jpg"]
        # positions = [(0, 0), (750, 0), (0, 550), (750, 550)]

        # for image_path, position in zip(images, positions):
        #     image = Image.open(image_path)
        #     photo = ImageTk.PhotoImage(image)
        #     label = tk.Label(parent_frame, image=photo)
        #     label.image = photo
        #     label.place(x=position[0], y=position[1])


##############
        
## 04/04/24 Addition to change size of image
        ### AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS'
        # top_left_image = Image.open("Chase.jpg")
        # desired_width = 200
        # desired_height = 200
        # resize_top_left_image = top_left_image.resize((desired_width, desired_height), Image.ANTIALIAS)

        # top_left_photo = ImageTk.PhotoImage(resize_top_left_image)
        # top_left_label = tk.Label(start_page, image=top_left_photo)
        # top_left_label.image = top_left_photo
        # top_left_label.place(x=0, y=0)


######
        
        # top_left_image = Image.open("Chase.jpg")
        # top_left_photo = ImageTk.PhotoImage(top_left_image)
        # top_left_label = tk.Label(start_page, image=top_left_photo)
        # top_left_label.image = top_left_photo
        # top_left_label.place(x=0, y=0)

        # top_right_image = Image.open("Marshall.jpg")
        # top_right_photo = ImageTk.PhotoImage(top_right_image)
        # top_right_label = tk.Label(start_page, image=top_right_photo)
        # top_right_label.image = top_right_photo
        # top_right_label.place(x=750, y=0)

        # bottom_left_image = Image.open("Rubble.jpg")
        # bottom_left_photo = ImageTk.PhotoImage(bottom_left_image)
        # bottom_left_label = tk.Label(start_page, image=bottom_left_photo)
        # bottom_left_label.image = bottom_left_photo
        # bottom_left_label.place(x=0, y=550)

        # bottom_right_image = Image.open("Zuma.jpg")
        # bottom_right_photo = ImageTk.PhotoImage(bottom_right_image)
        # bottom_right_label = tk.Label(start_page, image=bottom_right_photo)
        # bottom_right_label.image = bottom_right_photo
        # bottom_right_label.place(x=750, y=550)

    def create_time_selection_page(self):
        self.current_page = "time_selection"
        # self.destroy_previous_widgets()  # Clear the previous page
        time_selection_page = tk.Frame(self)
        time_selection_page.pack(fill=tk.BOTH, expand=True)

        # Time selection buttons
        five_sec_button = tk.Button(time_selection_page, text="5 Seconds", font=("Helvetica", 16),
                                    command=lambda: self.create_word_display_page(5))
        five_sec_button.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        thirty_sec_button = tk.Button(time_selection_page, text="30 Seconds", font=("Helvetica", 16),
                                      command=lambda: self.create_word_display_page(30))
        thirty_sec_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        one_min_button = tk.Button(time_selection_page, text="1 Minute", font=("Helvetica", 16),
                                   command=lambda: self.create_word_display_page(60))
        one_min_button.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(time_selection_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def create_word_display_page(self, duration):
        # OG Random letter generator

        import string
        import random

        # function to choose a random word from an imported list of words
        def generateRandomWord(words):
            return random.choice(words)

        wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
        #wordList = ['BATH', 'CARE', 'LOVE']
        randomWord = generateRandomWord(wordList)

        # print("Selected Word:", randomWord)

        # function to generate additional random letters as necessary by the 
        # length of the word chosen

        # 8 because we only have 8 tiles for letters
        remainingLetters = 8 - len(randomWord)

        # print("Letters To Fill:", remainingLetters)

        def removeLetters(letters2Remove):
            alphabet = list(string.ascii_uppercase)
            
            for letter in letters2Remove:
                if letter in alphabet:
                    alphabet.remove(letter)
            alphabetString = ''.join(alphabet)
            return alphabetString

        letters2Remove = randomWord
        availableLetters = removeLetters(letters2Remove)

        # print("Left Over Letters:", availableLetters)

        ## remove possibility of repeating letter by removing the randomly chosen letters from the list

        def generateRandomLetters(remainingLetters):
            # ensure no repeated letters:
            chosenLetters = random.sample(availableLetters, remainingLetters)
            return ''.join(chosenLetters)
            return ''.join(random.choices(string.ascii_uppercase, k=remainingLetters))
            
        randomLetters = generateRandomLetters(remainingLetters)

        # print("Random Letters:", randomLetters)

        # function to add all of the letters to one singular string

        def randomizeLetters(word, letters):
            allLetters = list(word + letters)
            random.shuffle(allLetters)
            return ''.join(allLetters)

        randomizedLetters = randomizeLetters(randomWord, randomLetters)

        # print("Final Letter Sequence:", randomizedLetters)
        ########################################## END RANDOM LETTERS
        
        self.current_page = "word_display"
        word_display_page = tk.Frame(self)
        word_display_page.pack(fill=tk.BOTH, expand=True)

        # Display word
        word_label = tk.Label(word_display_page, text=randomWord, font=("Helvetica", 48))
        word_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    # Actual Countdown Timer
    def create_countdown(self, frame, duration):
        countdown_label = tk.Label(frame, font=("Helvetica", 16))
        countdown_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

        def update_countdown(seconds_left):
            countdown_label.config(text=f"Time Left: {seconds_left} seconds")
            if seconds_left > 0:
                frame.after(1000, update_countdown, seconds_left - 1)
            else:
                self.create_gif_display_page()

        # could try update_countdown(int(duration)) ??
        update_countdown(duration)

    # GIF??
    def create_gif_display_page(self):
        self.current_page = "gif_display"
        gif_display_page = tk.Frame(self)
        gif_display_page.pack(fill=tk.BOTH, expand=True)

        # Add a label for text above the GIF
        text_label = tk.Label(gif_display_page, text="GIF Display Page", font=("Helvetica", 24))
        text_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        # Load and display the GIF
        gif_path = "MARSHALL.gif"
        gif_label = tk.Label(gif_display_page)
        gif_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        gif_image = PhotoImage(file=gif_path)
        gif_label.config(image=gif_image)
        gif_label.image = gif_image

        # Exit button
        exit_button = tk.Button(gif_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()