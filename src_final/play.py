import random
import string

from pygame import Color
from sound import Audio
from led import LED

# List of words used in the game
word_list = ['MY', 'THIS', 'A', 'IS', 'HOME','THE', 'IN', 'CITY', 'BY', 'OCEAN','ON', 'NOT', 'FARM', 'LIKE', 'I']

class GameLogic:
    def __init__(self):
        self.current_word = ""
        self.letter_map = {}  # Maps button numbers to letters
        self.chosen_letters = []  # Letters selected by the user so far
        self.led = LED()

    def get_new_word(self):
        """Selects a new random word from the word list."""
        self.current_word = random.choice(word_list).upper()  # Make sure word is uppercase
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
        self.letter_map = {i+1: letter for i, letter in enumerate(all_letters)}
        
        # Print keypad number-letter combinations & # Display LED on each tile
        for button_number, letter in self.letter_map.items():
            self.led.clear_all()
            self.led.display_letter(letter, button_number, Color(100, 100, 100))
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
            Audio.play_correct_letter()
            if len(self.chosen_letters) == len(self.current_word):
                return True, "Next word"
            return True, "Correct"
        else:
            if chosen_letter in self.current_word:
                self.led.display_letter(expected_letter, button_number, Color(0, 0, 255))
                Audio.play_wrong_order()  # Play wrong order sound
            else:
                self.led.display_letter(expected_letter, button_number, Color(255, 0, 0))
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
