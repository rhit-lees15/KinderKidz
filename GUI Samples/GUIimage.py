# from tkinter import *
# from tkinter.ttk import *

# image = PhotoImage(file = 'Carmine.png')
# label['image'] = image

import tkinter as tk
# from PIL(??????) import Image, ImageTk

class ImageDisplayApp:
    def __init__(self, master, image_path):
        self.master = master
        self.image_path = image_path
        
        # Load the image
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        
        # Create a label to display the image
        self.image_label = tk.Label(master, image=self.photo)
        self.image_label.pack()
        
        # Add a button to close the window
        self.close_button = tk.Button(master, text="Close", command=self.close_window)
        self.close_button.pack()
        
    def close_window(self):
        self.master.destroy()

def main():
    # Define the path to your image
    image_path = "Carmine.png"
    
    # Create the Tkinter application
    root = tk.Tk()
    root.title("Image Display App")
    
    # Create an instance of the ImageDisplayApp
    app = ImageDisplayApp(root, image_path)
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()

# pip install pillow
# sudo apt-get install python3-tk