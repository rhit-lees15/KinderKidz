import tkinter as tk
from tkinter import *
from tkinter import PhotoImage, messagebox, ttk
# from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import random
# from sound_w_game import * 

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
        start_page = tk.Frame(self, bg = 'black')
        start_page.pack(fill=tk.BOTH, expand=True)

        # Picture Left
        image_path = "./OLDCODE/Images/Carmine.PNG" # ./Images/name.type
        image = self.load_image(image_path)
        # resize_image = image.resize((50, 50))
        picture_label = tk.Label(start_page, image=image, borderwidth=0)
        picture_label.image = image
        picture_label.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        # # Picture Right
        image_path2 = "./OLDCODE/Images/COW.PNG"
        image2 = self.load_image(image_path2)
        picture_label2 = tk.Label(start_page, image=image2, borderwidth=0)
        picture_label2.image = image2
        picture_label2.place(relx=0.6, rely=0.5, anchor=tk.CENTER)

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
        time_selection_page = tk.Frame(self, bg = "black")
        time_selection_page.pack(fill=tk.BOTH, expand=True)

        # Time selection buttons
        first_time_button = tk.Button(time_selection_page, text="5 Seconds", font=("Helvetica", 20),
                                    bg = "black", fg = "white",
                                    command=lambda: self.create_word_display_page(5))
        first_time_button.place(relx=0.3, rely=0.5, anchor=tk.CENTER)

        second_time_button = tk.Button(time_selection_page, text="5 Minutes", font=("Helvetica", 20),
                                      bg = "black", fg = "white",
                                      command=lambda: self.create_word_display_page(300))
        second_time_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        third_time_button = tk.Button(time_selection_page, text="10 Minutes", font=("Helvetica", 20),
                                   bg = "black", fg = "white",
                                   command=lambda: self.create_word_display_page(600))
        third_time_button.place(relx=0.7, rely=0.5, anchor=tk.CENTER)

        # Exit button
        exit_button = tk.Button(time_selection_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["time_selection"] = time_selection_page  # Store the time selection page

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
                             bg = "black", fg = "white")
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
                self.create_dance_display_page()

        update_countdown(duration)

    def create_dance_display_page(self):
        self.hide_current_page()  # Hide current page
        self.current_page = "Dance_display"
        
        dance_display_page = tk.Frame(self, bg = "black")
        dance_display_page.pack(fill=tk.BOTH, expand=True)

        # Add a label for text above the GIF
        text_label = tk.Label(dance_display_page, text="Dance Display Page", font=("Helvetica", 24), bg = "black", fg = "white")
        text_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

        root = tk.Tk()

        root.title('Listbox')

        # create a list box
        songs = ('Song 1', 'Song 2', 'Song 3', 'Song 4')

        var = tk.Variable(value=songs)

        listbox = tk.Listbox(
            root,
            listvariable=var,
            height=6,
            selectmode=tk.EXTENDED)

        listbox.pack(expand=True, fill=tk.BOTH, side=tk.LEFT)

        # link a scrollbar to a list
        scrollbar = ttk.Scrollbar(
            root,
            orient=tk.VERTICAL,
            command=listbox.yview
        )

        listbox['yscrollcommand'] = scrollbar.set

        scrollbar.pack(side=tk.LEFT, expand=True, fill=tk.Y)

        def items_selected(event):
            # get selected indices
            selected_indices = listbox.curselection()
            # get selected items
            selected_songs = ",".join([listbox.get(i) for i in selected_indices])
            msg = f'You selected: {selected_songs}'
            # messagebox.askokcancel(f'You selected: {selected_songs},
            #                     Is this your final choice')

            showinfo(title='Information', message=msg)


        # listbox.bind('<<ListboxSelect>>', items_selected)

        # # Load and display the GIF
        # gif_path = "example.gif"  # Change this to your GIF path
        # gif_label = tk.Label(gif_display_page)
        # gif_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        # gif_image = PhotoImage(file=gif_path)
        # gif_label.config(image=gif_image)
        # gif_label.image = gif_image

        # Exit button
        exit_button = tk.Button(dance_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        self.pages["dance_display"] = dance_display_page  # Store the GIF display page

    def hide_current_page(self):
        if self.current_page in self.pages:
            self.pages[self.current_page].pack_forget()  # Withdraw the current page

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()   
    app.mainloop()
