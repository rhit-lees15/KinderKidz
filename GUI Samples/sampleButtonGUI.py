import tkinter as tk


def button_click():
    print("Button was clicked!")

def create_gui():
    # Create the main window
    window = tk.Tk()
    window.title("Main Window")

    # Create a button to open the pop-up window
    button = tk.Button(window, text="Open Pop-up", command=open_popup)
    button.pack()

    # Run the GUI
    window.mainloop()

def open_popup():
    # Create a new pop-up window
    popup = tk.Toplevel()
    popup.title("Pop-up Window")

    # Create a button in the pop-up window
    popup_button = tk.Button(popup, text="Click Me", command=button_click)
    popup_button.pack()

    # Run the pop-up window
    popup.mainloop()

# Call the function to create the GUI
create_gui()