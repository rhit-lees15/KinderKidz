import string
import random
from gpiozero import Button

# GPIO pin numbers for buttons
button_pins = [7, 24, 6]

# function to choose a random word from an imported list of words
def generateRandomWord(words):
    return random.choice(words)

word = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(word)

# Initialize buttons
buttons = [Button(pin) for pin in button_pins]

# Available uppercase random letters
def removeLetters(letters2Remove):
    alphabet = list(string.ascii_uppercase)
    
    for letter in letters2Remove:
        if letter in alphabet:
            alphabet.remove(letter)
    alphabetString = ''.join(alphabet)
    return alphabetString

availableLetters = removeLetters(randomWord)

# Random letters chosen
def generateRandomLetters(remainingLetters):
    # ensure no repeated letters:
    chosenLetters = random.sample(availableLetters, remainingLetters)
    return ''.join(chosenLetters)
    return ''.join(random.choices(string.ascii_uppercase, k=remainingLetters))
    
remainingLetters = 3 - len(randomWord)
randomLetters = generateRandomLetters(remainingLetters)

def randomizeLetters(word, letters):
    allLetters = list(word + letters)
    random.shuffle(allLetters)
    return ''.join(allLetters)

randomizedLetters = randomizeLetters(randomWord, randomLetters)

def get_random_letter(string_length):
    randLetters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(randLetters) for i in range(string_length))

def generate_options(correct_letter):
    options = [correct_letter]
    while len(options) < 3:
        letter = get_random_letter(1)
        if letter not in options:
            options.append(letter)
    random.shuffle(options)
    return options

def game():
    spellWord = randomWord
    word_index = 0
    
    while word_index < len(spellWord):
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

print('Spell out this word plz: ', randomWord)