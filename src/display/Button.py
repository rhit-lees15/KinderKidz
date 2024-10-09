# Display LEDS, and respond when pushed
from config import letters
from Media.GameSound import Audio
from display.DisplayManager import DisplayManager
# Raspberry Pi pin inputs that are used for each individual tile. 

# BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]
# Current ground pin for the buttons is at pin 20

class Button:
    
    def __init__(offset, strip, pin):
        offset = offset * 100
        strip = strip
        pin = pin

    def turn_on(current_pixel, color):
        strip.setPixelColor(current_pixel + offset, color)
        strip.show() 

    def turn_off(current_pixel, color):
        strip.setPixelColor(current_pixel + offset, Color(0, 0, 0))

    def display_letter(letter, color):
        # letter = 'A'
        lights = letters[letter]
        for light in lights:
            turn_on(light, color)
    
    def display_output(letter, is_correct):
    # might have to map in number to tiles_num by finding which index the pin is located at
        current_letter = [x + offset for x in letters[letter]]
        if (is_correct):
            display_letter(current_letter, Color(0, 250,0))
        else:
            display_letter(current_letter, Color(250, 0,0))

    # Function to generate additional random letters
    def generateRandomLetters(remainingLetters, numLetters):
        return random.sample(remainingLetters, numLetters)
    # Function to add all letters to one string and shuffle them
    def randomizeLetters(word, letters):
        allLetters = list(word + ''.join(letters))
        random.shuffle(allLetters)
        return ''.join(allLetters)
    
    # Function to handle button press event
    def buttonPress(pin):
        global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
        
        letter = button_letters[pin]
        # time.sleep(0.25)
        if letter in randomWord:
            # Check if the letter is in the correct position
            if letter == randomWord[len(spelledWord)]:
                ## The letter is in the word
                spelledWord += letter
                # print("Current spelling:", spelledWord)
                if len(spelledWord) != len(randomWord):
                    ## The letter is in correct position - correct
                    #correct_light(pin)
                    DisplayManager.correct_light(letter, pin)
                    Audio.play_happy()
                    Audio.play_correct_letter()
                # If the full word is spelled correctly
                elif len(spelledWord) == len(randomWord):
                    print("Correct! You spelled the word correctly.")
                    DisplayManager.correct_light(letter, pin)
                    Audio.play_happy()
                    DisplayManager.turn_off()
                    Audio.play_next_word()
                    newWord()
                    DisplayManager.initialize_letter(randomizedLetters)

            else:
                # Find the first incorrect letter position

                #incorrect_position = spelledWord[]
                # restart_from = randomWord.index(spelledWord[incorrect_position])
                if len(spelledWord) == 0:
                    # print("Incorrect order!")
                    #spelledWord = ''
                    Audio.play_wrong_order()
                    # print("Current spelling:", spelledWord)
                else:
                    #spelledWord = randomWord[incorrect_position]
                    # print("Incorrect order! Restarting from:", spelledWord)
                    Audio.play_wrong_order()
        else:
            # print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
            DisplayManager.wrong_light(letter, pin)
            Audio.play_wrong_letter()

    def newWord():
        global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
        
    ## NOOR NEW ADDITION 05.09.24
        word_list.remove(randomWord)
        
        if not word_list:
            print("Congratulations! You've spelled all the words in the list!")
            return
        
        
        ################# END OF ADDITION
        # Generate a new word
        n = 0
        while n <= len(word_list) - 1:
            randomWord = word_list[n]
            n += 1
        
        # Get remaining letters
        availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
        # availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
        # Generate additional random letters
        randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))
        
        # Combine the random word and random letters into a single string and shuffle them
        randomizedLetters = randomizeLetters(randomWord, randomLetters)
        
        # Map each letter to a button
        button_letters = {}
        for idx, pin in enumerate(BUTTON_PINS):
            button_letters[pin] = randomizedLetters[idx]
        
        # Set button sequence for the new word
        button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]
        
        # Print new word and letters
        # init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
        print("Let's spell another word.")
        print(f"Spell the word: {randomWord}")
        # print("Reallocated letters: " + ' '.join(randomizedLetters))
        # print("Available letters: " + ' '.join(availableLetters))
        
        # Reset spelledWord
        spelledWord = ''

        
