import RPi.GPIO as GPIO
import time

class Buttons:
    def __init__(self, button_pins, callback):
        """
        Initializes the GPIO buttons.

        :param button_pins: List of GPIO pins connected to buttons
        :param callback: Function to call when a button is pressed (pass the button number)
        """
        self.button_pins = button_pins
        self.callback = callback

        # Set up GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        # Set up each button pin as an input with a pull-up resistor
        for pin in self.button_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # Add event detection for each pin
        for idx, pin in enumerate(self.button_pins):
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=lambda x, idx=idx: self.button_pressed(idx + 1), bouncetime=300)

    def button_pressed(self, button_number):
        """
        Called when a button is pressed.
        Passes the button number to the callback function.
        """
        print(f"Button {button_number} pressed.")
        self.callback(button_number)

    def cleanup(self):
        """Cleans up the GPIO settings when exiting the game."""
        GPIO.cleanup()
