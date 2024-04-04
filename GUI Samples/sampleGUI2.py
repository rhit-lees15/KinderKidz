import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import tkinter.font
import time
from PIL import Image, ImageTk

def start_game():
    global game_window
    game_window = tk.Tk()
    game_window.attributes('-fullscreen', True)

    # exit cleanly
    def close(event = None):
        game_window.destroy()

    # Bind escape key to cose?
    game_window.bind('<Escape>', close)

    # Display the timer
    timer_label = tk.Label(game_window, text = "", font = myFont)
    timer_label.pack(anchor = "ne", padx = 10, pady = 10)
    start_time = time.time()
    update_timer(timer_label, start_time)

    # exit cleanly
    game_window.protocol("WM_DELETE_WINDOW", close)

    # Start the GUI event loop for the game window
    game_window.mainloop()

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
        self.current_page = "word_display"
        word_display_page = tk.Frame(self)
        word_display_page.pack(fill=tk.BOTH, expand=True)

        # Display word
        word_label = tk.Label(word_display_page, text="WORD", font=("Helvetica", 48))
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
            self.exit_program()

    # could try update_countdown(int(duration)) ??
    update_countdown(duration)

def update_timer(label, start_time):
    # Set the duration of the timer here (in seconds)
    timer_duration = 10  # 5 minutes by default - 300
    elapsed_time = int(time.time() - start_time)
    remaining_time = max(0, timer_duration - elapsed_time)
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    label.config(text=f"Time left: {minutes:02d}:{seconds:02d}")
    if remaining_time > 0:
        label.after(1000, update_timer, label, start_time)
    else:
        label.config(text="Time's up!")
        game_window.after(2000, exit_program)

# Create the main window
root = tk.Tk()
root.attributes('-fullscreen', True)

# Create a font
myFont = tkinter.font.Font(family='Helvetica', size=12, weight="bold")

# Create a frame for the start page
start_frame = tk.Frame(root)
start_frame.pack(fill=tk.BOTH, expand=True)

# Display the image on the start page
# Replace 'image_path' with the actual path to your image file
# image_path = 'Carmine.png'
# start_img = tk.PhotoImage(file=image_path)
# start_img = start_img.subsample(2)  # Half the size
# start_img_label = tk.Label(start_frame, image=start_img)
# start_img_label.pack(side="left", padx=10, pady=10)

# Create a button to start the game
start_button = tk.Button(start_frame, text="START", font=myFont, command=start_game, bg='sea green', fg='#FFFFFF',
                         height=5, width=26)
start_button.pack(side="left", padx=10, pady=10)

    # # Exit button
    # exit_button = tk.Button(start_page, text="Exit", bg="red", font=("Helvetica", 16),
    #                         command=self.exit_program)
    # exit_button.place(relx=0.5, rely=0.95, anchor=tk.CENTER)

# exit button
exitButton = tk.Button(root, text="Exit", font=myFont, command=root.destroy, bg='brown4', height=1, width=52)
exitButton.pack(side="bottom")

# Bind escape key to exit the game
root.bind('<Escape>', root.destroy)

# Start the GUI event loop for the main window
root.mainloop()