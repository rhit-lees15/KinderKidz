import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import threading

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Interactive GUI")
        self.geometry("600x400")

        self.current_page = None
        self.timer_thread = None

        self.start_page()

    def start_page(self):
        # Clear previous page
        if self.current_page:
            self.current_page.destroy()

        # Create start page
        self.current_page = tk.Frame(self, bg="white", width=600, height=400)
        self.current_page.pack_propagate(0)
        self.current_page.pack()

        # Load images
        image_paths = ["Chase.jpg", "Marshall.jpg", "Rubble.jpg", "Zuma.jpg"]
        ## doesn't like this line
        images = [Image.open(path).resize((100, 100), Image.ANTIALIAS) for path in image_paths]
        self.image_labels = [tk.Label(self.current_page, image=ImageTk.PhotoImage(image=img)) for img in images]

        # Place images in the four corners
        self.image_labels[0].place(x=0, y=0)
        self.image_labels[1].place(x=500, y=0)
        self.image_labels[2].place(x=0, y=300)
        self.image_labels[3].place(x=500, y=300)

        # Start button
        start_button = tk.Button(self.current_page, text="Start", command=self.time_page, bg="green", font=("Arial", 16))
        start_button.place(relx=0.5, rely=0.5, anchor="center")

        # Exit button
        exit_button = tk.Button(self.current_page, text="Exit", command=self.exit_app, bg="red", font=("Arial", 16))
        exit_button.place(relx=0.5, rely=0.95, anchor="center")

    def time_page(self):
        # Clear previous page
        if self.current_page:
            self.current_page.destroy()

        # Create time selection page
        self.current_page = tk.Frame(self, bg="white", width=600, height=400)
        self.current_page.pack_propagate(0)
        self.current_page.pack()

        # Time buttons
        time_options = [("5 seconds", 5), ("30 seconds", 30), ("1 minute", 60)]
        for text, seconds in time_options:
            button = tk.Button(self.current_page, text=text, command=lambda s=seconds: self.word_page(s), font=("Arial", 16))
            button.pack(pady=10)

        # Exit button
        exit_button = tk.Button(self.current_page, text="Exit", command=self.exit_app, bg="red", font=("Arial", 16))
        exit_button.pack(side="bottom", pady=20)

    def word_page(self, seconds):
        # Clear previous page
        if self.current_page:
            self.current_page.destroy()

        # Create word display page
        self.current_page = tk.Frame(self, bg="white", width=600, height=400)
        self.current_page.pack_propagate(0)
        self.current_page.pack()

        # Countdown clock
        self.remaining_time = seconds
        self.clock_label = tk.Label(self.current_page, text=f"Time Remaining: {self.remaining_time}s", font=("Arial", 12))
        self.clock_label.place(x=500, y=10)

        # Start countdown thread
        self.timer_thread = threading.Thread(target=self.countdown)
        self.timer_thread.start()

        # Word display
        word_label = tk.Label(self.current_page, text="Hello", font=("Arial", 36))
        word_label.place(relx=0.5, rely=0.5, anchor="center")

        # Exit button
        exit_button = tk.Button(self.current_page, text="Exit", command=self.exit_app, bg="red", font=("Arial", 16))
        exit_button.pack(side="bottom", pady=20)

    def countdown(self):
        while self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            self.clock_label.config(text=f"Time Remaining: {self.remaining_time}s")
        self.show_gif()

    def show_gif(self):
        # Clear previous page
        if self.current_page:
            self.current_page.destroy()

        # Create GIF display page
        self.current_page = tk.Frame(self, bg="white", width=600, height=400)
        self.current_page.pack_propagate(0)
        self.current_page.pack()

        # Load and display GIF
        gif_label = tk.Label(self.current_page, text="GIF Display", font=("Arial", 24))
        gif_label.place(relx=0.5, rely=0.1, anchor="center")

        # Exit button
        exit_button = tk.Button(self.current_page, text="Exit", command=self.exit_app, bg="red", font=("Arial", 16))
        exit_button.pack(side="bottom", pady=20)

    def exit_app(self):
        # Confirm exit
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.destroy()

if __name__ == "__main__":
    app = GUI()
    app.mainloop()