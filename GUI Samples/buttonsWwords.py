## 

import random
from gpiozero import Button

# GPIO pin numbers for buttons
button_pins = [17, 18, 27]

# List of three-letter words
words = ["cat", "dog", "bat"]

# Initialize buttons
buttons = [Button(pin) for pin in button_pins]

def get_random_letter():
    return chr(random.randint(97, 122))  # Random lowercase letter

def generate_options(correct_letter):
    options = [correct_letter]
    while len(options) < 3:
        letter = get_random_letter()
        if letter not in options:
            options.append(letter)
    random.shuffle(options)
    return options

def game():
    word = random.choice(words)
    word_index = 0
    
    while word_index < len(word):
        correct_letter = word[word_index]
        options = generate_options(correct_letter)
        
        print(f"Spell the word: {' '.join(options)}")
        
        # Assign options to buttons
        for i, button in enumerate(buttons):
            button.wait_for_press()
            if button.pin.number == options.index(correct_letter):
                print("Correct!")
                word_index += 1
            else:
                print("Incorrect!")
        print("")  # Empty line for readability

game()
