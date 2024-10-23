import RPi.GPIO as GPIO
import random
import time

# GPIO setup
BUTTON_PINS = [24, 25, 23, 22, 5, 6, 13, 12]  # 8 GPIO pins connected to switches
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PINS, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Setup buttons with pull-up resistors

class Buttons:
    def __init__(self, word_list):
        self.word_list = word_list
        self.current_word = random.choice(self.word_list)
        self.correct_index = 0
        self.letter_assignments = {}
        self.assign_letters()

        # Assign callbacks for button presses
        for pin in BUTTON_PINS:
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.handle_gpio_input, bouncetime=300)

    def assign_letters(self):
        """Randomly assign letters to GPIO pins."""
        letters = list(self.current_word) + random.sample('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 8 - len(self.current_word))
        random.shuffle(letters)

        # Map letters to the GPIO pins
        self.letter_assignments = {BUTTON_PINS[i]: letters[i] for i in range(8)}
        print("Current letter assignments:", self.letter_assignments)

    def handle_gpio_input(self, pin):
        """Handle button press on GPIO pins."""
        letter = self.letter_assignments.get(pin)
        if not letter:
            return  # No letter assigned to this pin

        print(f"Button {pin} pressed. Letter: {letter}")
        
        if letter == self.current_word[self.correct_index]:
            print("Correct!")
            self.correct_index += 1

            if self.correct_index == len(self.current_word):
                print("Word completed! Moving to next word.")
                self.next_word()
        else:
            if letter in self.current_word:
                print("Wrong order! Try again.")
            else:
                print("Wrong letter!")

    def next_word(self):
        """Go to the next word and reset everything."""
        self.current_word = random.choice(self.word_list)
        self.correct_index = 0
        self.assign_letters()

    def cleanup(self):
        """Cleanup GPIO pins when game is over."""
        GPIO.cleanup()

# Example usage:
if __name__ == "__main__":
    word_list = ["I", "Home", "Ocean", "They", "Me", "Cat", "Dog", "Lion", "Pig", "Cow"]
    game = PlayGameGPIO(word_list)

    try:
        # Game loop - just to keep the program running
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Exiting game.")
    finally:
        game.cleanup()
