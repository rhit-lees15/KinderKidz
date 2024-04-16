## 

import string
import random
from gpiozero import Button

# GPIO pin numbers for buttons
button_pins = [7, 24, 6]

# List of three-letter words
words = ['CAT', 'DOG']

# Initialize buttons
buttons = [Button(pin) for pin in button_pins]

def removeLetters(letters2Remove):
    alphabet = list(string.ascii_uppercase)
    
    for letter in letters2Remove:
        if letter in alphabet:
            alphabet.remove(letter)
    alphabetString = ''.join(alphabet)
    return alphabetString

letters2Remove = randomWord
availableLetters = removeLetters(letters2Remove)

def get_random_letter(remainingLetters):
    # ensure no repeated letters:
    chosenLetters = random.sample(availableLetters, remainingLetters)
    return ''.join(chosenLetters)
    return ''.join(random.choices(string.ascii_uppercase, k=remainingLetters))
    
randomLetters = get_random_letter(remainingLetters)

# def get_random_letter():
#     return chr(random.randint(97, 122))  # Random lowercase letter

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
                print({' '.join(correct_letter)})
            else:
                print("Incorrect! Try again!")
        print("")  # Empty line for readability

game()
