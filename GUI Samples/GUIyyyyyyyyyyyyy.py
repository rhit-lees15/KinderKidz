import tkinter as tk
import tkinter.font

def button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()

# Set window size and position it in the center
window_width = 300
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Create a button
button = tk.Button(root, text = "Click Me!", command = button_click)
button.place(relx = 1, rely = 1, anchor = "center")  # Placing button in the center

def close():
    root.destroy()

## FONT
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## exit button
exitButton = tk.Button(root, text = "Exit", font = myFont, command = close, bg = 'red', height = 1, width = 26)
#exitButton.grid(row = 1, column = 1)

# exit cleanly
root.protocol("WM_DELETE_WINDOW", close)

# Start the GUI event loop
root.mainloop()
