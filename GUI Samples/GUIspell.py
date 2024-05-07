import tkinter as tk
from tkinter import PhotoImage, messagebox
import random
# from sound_w_game import *

class GUI(tk.Tk):
    def create_word_display_page(self, duration):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"

        # Generate a new random word
        newWord()

        # Get the random word
        random_word = spelledWord
       
        # Display word
        word_display_page = tk.Frame(self, bg="black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=random_word, font=("Helvetica", 48),
                             bg="black", fg="white", )
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["word_display"] = word_display_page  # Store the word display page
    
    def create_word_display_page(self, duration):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"



        # Random word generator
        word_list = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
        random_word = random.choice(word_list)

        # Display word
        word_display_page = tk.Frame(self, bg = "black")
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Label(word_display_page, text=random_word, font=("Helvetica", 48),
                             bg = "black", fg = "white",)
        word_text.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # # Change color of each letter
        # colors = ["red", "blue", "green", "purple", "orange"]  # List of colors
        # for i, letter in enumerate(random_word):
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

        def update_countdown(seconds_left):
            countdown_label.config(text=f"Time Left: {seconds_left} seconds", bg = "black", fg = "white")
            if seconds_left > 0:
                frame.after(1000, update_countdown, seconds_left - 1)
            else:
                self.create_gif_display_page()

        update_countdown(duration)

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()   
    app.mainloop()
