from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Open the image
image = Image.open("./OLDCODE/Image/Carmine.PNG")

# Resize the image, passing the size as a tuple (width, height)
resize_image = image.resize((50, 50))

# Convert the resized image into a Tkinter-compatible format
img = ImageTk.PhotoImage(resize_image)

# Create a label and add the image
label1 = Label(image=img)
label1.image = img  # Keep a reference to avoid garbage collection
label1.pack()

root.mainloop()