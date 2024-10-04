import tkinter as tk
from tkinter import PhotoImage, messagebox, ttk
from tkinter.messagebox import showinfo
import random
import time
# Doesn't like this line
# from GameManager import create_countdown
# import vlc

# Dictionary of all the words included in the spelling game
word_lists = {
    "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
    "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
    "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
    }

class GUI(tk.TK):
    
    # def __call__(self, ...):
    # return GUI(...)
    
    # class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive GUI")
        self.attributes('-fullscreen', True)  # Make the GUI full screen

        self.current_page = None
        self.pages = {}  # Dictionary to store pages

        self.create_start_page()

    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self, bg = 'black')
        start_page.pack(fill=tk.BOTH, expand=True)

        # Central Picture ******************* TODO rename the file locations of the pictures ***************************
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

    def load_image(self, path):
        image = tk.PhotoImage(file=path)
        return image

    def create_list_selection_page(self):
        self.hide_current_page()  # Hide current page

        self.current_page = "list_selection"
        list_selection_page = tk.Frame(self, bg="black")
        list_selection_page.pack(fill=tk.BOTH, expand=True)

        # Label for word list selection
        list_label = tk.Label(list_selection_page, text="Select a Word List:", font=("Helvetica", 20), bg="black", fg="white")
        list_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

       # On-screen button to select first word list
        first_list_button = tk.Button(list_selection_page, text="List 1", font=("Helvetica", 40),
                                    bg="blue", fg="white", command=lambda: self.create_word_display_page("List 1"))
        first_list_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

        # On-screen button to select second word list
        second_list_button = tk.Button(list_selection_page, text="List 2", font=("Helvetica", 40),
                                    bg="green", fg="white", command=lambda: self.create_word_display_page("List 2"))
        second_list_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # On-screen button to select third word list
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

        # Display word
        word_display_page = tk.Frame(self, bg="black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        random_word = random.choice(word_list_name)

        word_text = tk.Label(word_display_page, text=random_word, font=("Helvetica", 48),
                            bg="black", fg="white")
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        duration = 30

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
        
        # Display word
        word_display_page = tk.Frame(self, bg = "black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=random_word, font=("Helvetica", 48),
                             bg = "black", fg = "white")
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["word_display"] = word_display_page  # Store the word display page

    # Function to switch back to word display after the song finishes
    def back_to_word_display(word_list_name):
        # Destroy the dance display page
        app.pages["dance_display"].destroy()
        # Re-create the word display page
        app.create_word_display_page(word_list_name)
        pass

    def create_dance_display_page(self):
        self.hide_current_page()  # Hide current page
        self.current_page = "Dance_display"
        dance_display_page = tk.Frame(self, bg="black")
        dance_display_page.pack(fill=tk.BOTH, expand=True)

        # Label for word list selection -- this does not show up, and unsure as to why
        dance_label = tk.Label(dance_display_page, text="Select a Song:", font=("Helvetica", 20), bg="black", fg="white")
        dance_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

        # Create a Listbox
        songs = ('Song 1', 'Song 2', 'Song 3', 'Song 4')
        listbox = tk.Listbox(dance_display_page, height=6, selectmode=tk.EXTENDED, bg="black", fg="white", font=("Helvetica", 24))
        listbox.pack(side=tk.LEFT, padx=0, pady=20, fill=tk.BOTH, expand=True)

        for song in songs:
            listbox.insert(tk.END, song)

        # Link a scrollbar to the Listbox
        scrollbar = ttk.Scrollbar(dance_display_page, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

        # Function to handle song selection
        def play_song():
            selected_song_index = listbox.curselection()
            if selected_song_index:
                selected_song = songs[selected_song_index[0]]  # Get the selected song
                # play_selected_song(selected_song)

        # Button to play the selected song
        play_button = tk.Button(dance_display_page, text="Play", bg="green", font=("Helvetica", 16), command=play_song)
        play_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(dance_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["dance_display"] = dance_display_page  # Store the data

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()