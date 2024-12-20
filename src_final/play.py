import random
import string
from sound import Audio
from led import LED
from pygame import Color

# List of words used in the game
word_list = ["Home", "Ocean", "They", "Me", "Cat", "Dog", "Lion", "Pig", "Cow"]

class GameLogic:
    def __init__(self):
        self.current_word = ""
        self.letter_map = {}  # Maps button numbers to letters
        self.chosen_letters = []  # Letters selected by the user so far
        self.led = LED()
        self.used_words = set()

    def get_new_word(self):
        """Selects a new random word from the word list."""
        self.led.clear_all() #reseting LED display

        if len(self.used_words) == len(word_list):
            print("All words used. Game Over!")
            # return None # Change this so that the game starts over
            self.used_words.clear()
            
        while True:
            new_word = random.choice(word_list).upper()  # Make sure word is uppercase
            if new_word not in self.used_words:
                self.used_words.add(new_word)
                self.current_word = new_word
                self.chosen_letters = []  # Reset user input
                return self.current_word

    def generate_buttons(self):
        """
        Randomly assigns letters to the 8 buttons.
        Ensures that all letters from the current word are included.
        """
        if not self.current_word:
            raise ValueError("No current word set. Call get_new_word() first.")
        
        # Choose random letters to fill the rest of the buttons
        remaining_letters = list(set(string.ascii_uppercase) - set(self.current_word))
        random.shuffle(remaining_letters)
        
        # Fill the 8 buttons with letters from the current word and some random letters
        all_letters = list(self.current_word) + remaining_letters[:8 - len(self.current_word)]
        random.shuffle(all_letters)
        
        # Map button numbers (1-8) to letters
        self.letter_map = {i: letter for i, letter in enumerate(all_letters)}
        
        # Print keypad number-letter combinations
        for button_number, letter in self.letter_map.items():
            # self.led.display_letter(letter, button_number, Color(255, 235, 128)) # warm light
            # self.led.display_letter(letter, button_number, Color(100, 100, 100)) # standard white light
            self.led.display_letter(letter, button_number, Color(128, 180, 160)) # cool light


            print(f"Button {button_number}: {letter}")
        
        # Return the mapping of button numbers to letters for display
        return self.letter_map

    def check_input(self, button_number):
        """
        Checks if the letter chosen via the button is the correct next letter in the word.
        """
        if button_number not in self.letter_map:
            return False, "Invalid button number."

        chosen_letter = self.letter_map[button_number]
        expected_letter = self.current_word[len(self.chosen_letters)]
        
        if chosen_letter == expected_letter:
            self.chosen_letters.append(chosen_letter)
            self.led.display_letter(expected_letter, button_number, Color(0, 255, 0))
            Audio.play_happy()
            Audio.play_correct_letter()
            if len(self.chosen_letters) == len(self.current_word):
                Audio.play_next_word()
                return True, "Next word"
            return True, "Correct"
        else:
            if chosen_letter in self.current_word:
                self.led.display_letter(chosen_letter, button_number, Color(255, 155, 0))
                Audio.play_wrong_order()  # Play wrong order sound
            else:
                self.led.display_letter(chosen_letter, button_number, Color(255, 0, 0))
                Audio.play_wrong_letter()  # Play wrong letter sound
            return False, "Try again"
        
    def get_word_list():
        return word_list
        
    @staticmethod
    def add_word(new_word):
        """Adds a new word to the word list."""
        new_word = new_word.strip()
        if new_word and new_word not in word_list:
            word_list.append(new_word.upper())
            print(f"Added new word: {new_word.upper()}")
