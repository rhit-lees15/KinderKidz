import tkinter as tk
import tkinter.font
import time

def start_game():
    global game_window
    game_window = tk.Tk()
    game_window.attributes('-fullscreen', True)

    # Function to exit the game cleanly
    def close(event=None):
        game_window.destroy()

    # Bind escape key to exit the game
    game_window.bind('<Escape>', close)

    # Display the timer
    timer_label = tk.Label(game_window, text="", font=myFont)
    timer_label.pack(anchor="ne", padx=10, pady=10)
    start_time = time.time()
    update_timer(timer_label, start_time)

    # Display text in the center
    text_label = tk.Label(game_window, text="Game Started!", font=myFont)
    text_label.pack(expand=True)

    # exit button
    exitButton = tk.Button(game_window, text="Exit", font=myFont, command=close, bg='brown4', height=1, width=52)
    exitButton.pack(side="bottom")

    # exit cleanly
    game_window.protocol("WM_DELETE_WINDOW", close)

    # Start the GUI event loop for the game window
    game_window.mainloop()

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
        game_window.after(2000, play_dance_party)

def play_dance_party():
    global game_window
    game_window.destroy()

    dance_window = tk.Tk()
    dance_window.attributes('-fullscreen', True)

    # Display "Dance Party" text
    dance_label = tk.Label(dance_window, text="Dance Party", font=myFont, pady=50)
    dance_label.pack()

    # Load and display the GIF
    gif_path = 'MARSHALL.gif'
    gif = tk.PhotoImage(file=gif_path)
    gif_label = tk.Label(dance_window, image=gif)
    gif_label.pack(expand=True)

    # Function to exit cleanly
    def close(event=None):
        dance_window.destroy()

    # Bind escape key to exit cleanly
    dance_window.bind('<Escape>', close)

    # Start the GUI event loop for the dance window
    dance_window.mainloop()

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
image_path = 'Carmine.png'
start_img = tk.PhotoImage(file=image_path)
start_img = start_img.subsample(2)  # Half the size
start_img_label = tk.Label(start_frame, image=start_img)
start_img_label.pack(side="left", padx=10, pady=10)

# Create a button to start the game
start_button = tk.Button(start_frame, text="START", font=myFont, command=start_game, bg='sea green', fg='#FFFFFF',
                         height=5, width=26)
start_button.pack(side="left", padx=10, pady=10)

# exit button
exitButton = tk.Button(root, text="Exit", font=myFont, command=root.destroy, bg='brown4', height=1, width=52)
exitButton.pack(side="bottom")

# Bind escape key to exit the game
root.bind('<Escape>', root.destroy)

# Start the GUI event loop for the main window
root.mainloop()