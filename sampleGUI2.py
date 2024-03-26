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

## Widgets
# ledButton = Button(win, text = "Turn LED On", font = myFont, command = ledToggle, bg = 'bisque2', height = 1, width = 24)
