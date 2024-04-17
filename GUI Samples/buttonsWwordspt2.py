# import string
# import random
import RPi.GPIO as GPIO
import time
from gpiozero import Button

# GPIO pin numbers for buttons
BUTTON_PIN = ([7, 24, 6])

#  Use the GPIO number instead of the Raspberry Pi number
GPIO.setmode(GPIO.BCM)

# Don't use resistor, rather use internal one
# Don't press, state (high) = 3.3 V
# Press, state (low) = 0 V
GPIO.setup(BUTTON_PIN[0], GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN[1], GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN[2], GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Will give a value
Button_1 = GPIO.input(BUTTON_PIN[0])
Button_2 = GPIO.input(BUTTON_PIN[1])
Button_3 = GPIO.input(BUTTON_PIN[2])

try:
    while True:
        time.sleep(0.1)
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            print("Button is pressed")
        else:
            print("Button is not pressed")
except KeyboardInterrupt:
    # Press Ctrl + C -> to exit code
    # Best practice, clean any GPIO, could burn pins
    GPIO.cleanup()

# Terminal
# find folder
    # fjlkadjfla/
    # python3 buttonPressTest.py