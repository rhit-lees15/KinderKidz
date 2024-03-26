# sudo apt-get install python3-tk --> run on Raspberry Pi first

import tkinter as tk

def open_popup():
    # Pop-up window
    popup = tk.Toplevel()
    popup.title("Pop-up BLAHALALAHALAH")

    # Label widget
    label = tk.Label(popup, text = "Hello, popup stuff")
    label.pack()

def create_gui():
    # Main window
    window = tk.Tk()
    window.title("Window BLAHLAHLAHLHAH")

    # Label widget
    button = tk.Button(window, text = "Open Pop-up", command = open_popup)
    button.pack()

    # Run the GUI
    window.mainloop()

create_gui