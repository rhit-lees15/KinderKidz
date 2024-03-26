# Advanced Test for the button 

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 16

# Use the GPIO number instead of the Raspberry Pi number
GPIO.setmode(GPIO.BCM)

# Don't use resistor, rather use internal one
# Don't press, state (high) = 3.3 V
# Press, state (low) = 0 V
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

# Will give a value
previous_button_state = GPIO.input(BUTTON_PIN)

try:
    while True:
        # Constant loop that probs isn't the best when running other code
        time.sleep(0.01)
        button_state = GPIO.input(BUTTON_PIN)
        if button_state != previous_button_state:
            previous_button_state = button_state
            if button_state == GPIO.HIGH:
                print("Button has just been released")
except KeyboardInterrupt:
    # Press Ctrl + C -> to exit code
    # Best practice, clean any GPIO, could burn pins
    GPIO.cleanup()

# Terminal
# find folder
    # fjlkadjfla/
    # python3 buttonPressTest.pytime.sleep(0.01)