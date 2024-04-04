import tkinter as tk
import tkinter.font

## FUTURE NOTICE: This will probs change to the next section where the game starts & audio plays
def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()

## FONT
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

# Set window size and position it in the center
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a button
button = tk.Button(root, text = "START", font = myFont, command = button_click, bg = 'sea green', fg = '#FFFFFF', height = 5, width = 26)
button.place(relx = 0.5, rely = 0.5, anchor = "center")  # Placing button in the center

def close():
    root.destroy()

## exit button
exitButton = tk.Button(root, text = "Exit", font = myFont, command = close, bg = 'brown4', height = 1, width = 52)
exitButton.pack(side = "bottom")

# exit cleanly
root.protocol("WM_DELETE_WINDOW", close)

# Start the GUI event loop
root.mainloop()
