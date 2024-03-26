from tkinter import *
import tkinter.font
# from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

# hardware
# led = LED(14)

# GUI DEFINITIONS
win = Tk()
win.title("Trial")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

## EVENT FUNCTIONS
def ledToggle():
    if led.is_lit: 
        led.off()
        ledButton["text"] = "Turn LED On"
    else:
        led.on()
        ledButton["text"] = "Turn LED off"

def close():
    RPi.GPIO.cleanup()
    win.destroy()

## Widgets
ledButton = Button(win, text = "Turn LED On", font = myFont, command = ledToggle, bg = 'bisque2', height = 1, width = 24)
ledButton.grid(row = 0, column = 1)

## exit button
exitButton = Button(win, text = "Exit", font = myFont, command = close, bg = 'red', height = 1, width = 26)
exitButton.grid(row = 1, column = 1)

# exit cleanly
win.protocol("WM_DELETE_WINDOW", close)

# Loop forever (Keep the GUI running)
win.mainloop()