import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import time
from PIL import Image, ImageTk

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("1600x800")
        self.title("Interactive GUI")

        self.current_page = None
        self.create_start_page()

    def create_start_page(self):
        self.current_page = "start"
        start_page = tk.Frame(self)
        start_page.pack(fill=tk.BOTH, expand=True)

        start_button = tk.Button(start_page, text="Start", bg="green", font=("Helvetica", 16),
                                 command=self.create_time_selection_page)
        start_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        exit_button = tk.Button(start_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

        # # Displaying images in the four corners
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
        time_selection_page = tk.Frame(self)
        time_selection_page.pack(fill=tk.BOTH, expand=True)

        five_sec_button = tk.Button(time_selection_page, text="5 Seconds", font=("Helvetica", 16),
                                    command=lambda: self.create_word_display_page(5))
        five_sec_button.place(relx=0.3, rely=0.4, anchor=tk.CENTER)

        thirty_sec_button = tk.Button(time_selection_page, text="30 Seconds", font=("Helvetica", 16),
                                      command=lambda: self.create_word_display_page(30))
        thirty_sec_button.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        one_min_button = tk.Button(time_selection_page, text="1 Minute", font=("Helvetica", 16),
                                   command=lambda: self.create_word_display_page(60))
        one_min_button.place(relx=0.7, rely=0.4, anchor=tk.CENTER)

        exit_button = tk.Button(time_selection_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def create_word_display_page(self, duration):
        self.current_page = "word_display"
        word_display_page = tk.Frame(self)
        word_display_page.pack(fill=tk.BOTH, expand=True)

        word_label = tk.Label(word_display_page, text="WORD", font=("Helvetica", 48))
        word_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.create_countdown(word_display_page, duration)

        exit_button = tk.Button(word_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

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

        exit_button = tk.Button(gif_display_page, text="Exit", bg="red", font=("Helvetica", 16),
                                command=self.exit_program)
        exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

    def exit_program(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()