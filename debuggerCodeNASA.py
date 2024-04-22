import tkinter as tk
from tkinter import PhotoImage, messagebox
import random

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Interactive GUI")
        self.attributes('-fullscreen', True)  # Make the GUI full screen

        self.current_page = None
        self.pages = {}  # Dictionary to store pages

        self.create_start_page()

    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self)
        start_page.pack(fill=tk.BOTH, expand=True)

        # Load and display images in the four corners of the GUI
        # images = ["Chase.jpg", "Marshall.jpg", "Rubble.jpg", "Zuma.jpg"]
        # positions = [(0, 0), (0, self.winfo_screenheight() - 375), (self.winfo_screenwidth() - 375, 0), (self.winfo_screenwidth() - 375, self.winfo_screenheight() - 375)]

        # for image_path, position in zip(images, positions):
        #     image = self.load_image(image_path)
        #     label = tk.Label(start_page, image=image)
        #     label.image = image
        #     label.place(x=position[0], y=position[1])

        # Start button
        start_button = tk.Button(start_page, text="Start", bg="green", font=("Helvetica", 25),
                                 command=self.create_time_selection_page)
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(start_page, text="Exit", bg="red", font=("Helvetica", 20),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["start"] = start_page  # Store the start page

    def load_image(self, path):
        image = tk.PhotoImage(file=path)
        return image

    def create_time_selection_page(self):
        self.hide_current_page()  # Hide current page
        self.current_page = "time_selection"
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

        self.pages["time_selection"] = time_selection_page  # Store the time selection page

    def create_word_display_page(self, duration):
        self.hide_current_page()  # Hide current page
        self.current_page = "word_display"

        # Random word generator
        word_list = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
        random_word = random.choice(word_list)

        # Display word
        word_display_page = tk.Frame(self)
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_text = tk.Text(word_display_page, font=("Helvetica", 48))
        word_text.insert(tk.END, random_word)
        word_text.config(state=tk.DISABLED)  # Disable editing
        word_text.pack(expand=True)

        # Highlight letters one by one
        self.highlight_letters(word_text, random_word)

        # Create countdown
        self.create_countdown(word_display_page, duration)

        # Exit button
        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["word_display"] = word_display_page  # Store the word display page

    def highlight_letters(self, text_widget, word):
        for i, char in enumerate(word):
            index = f"1.{i}"  # Index for the character in the text widget
            text_widget.tag_add("highlight", index, f"{index}+1c")  # Add tag to the character
            text_widget.tag_config("highlight", foreground="red")  # Configure the tag
            text_widget.after(1000 * (i + 1), lambda: self.remove_highlight(text_widget, index))  # Schedule removal of highlight

    def remove_highlight(self, text_widget, index):
        text_widget.tag_remove("highlight", index, f"{index}+1c")  # Remove highlight tag

    def create_countdown(self, frame, duration):
        countdown_label = tk.Label(frame, font=("Helvetica", 16))
        countdown_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

        def update_countdown(seconds_left):
            countdown_label.config(text=f"Time Left: {seconds_left} seconds")
            if seconds_left > 0:
                frame.after(1000, update_countdown, seconds_left - 1)
            else:
                self.create_gif_display_page()

        update_countdown(duration)

    def create_gif_display_page(self):
        self.hide_current_page()  # Hide current page
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

        self.pages["gif_display"] = gif_display_page  # Store the GIF display page

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
