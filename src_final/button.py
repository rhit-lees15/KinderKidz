# Display LEDS, and respond when pushed
# from config import letters
# from Media.GameSound import Audio
import random
import RPi.GPIO as GPIO 
# Raspberry Pi pin inputs that are used for each individual tile. 

# BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]
# Current ground pin for the buttons is at pin 20

BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]

GPIO.setmode(GPIO.BCM)
for pin in BUTTON_PINS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda pin: buttonPress(pin), bouncetime=1000)
