# Test 3

from signal import pause
from gpiozero import LED, Button

button = Button(16)

try:
    #button.when_pressed = ...

    pause()

finally:
    pass