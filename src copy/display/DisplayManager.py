from pygame import Color
# from config import letters
from display.Button import Button

# import letters from config
# import Button from Button

class DisplayManager:

    LED_COUNT      = 800      # Number of LED pixels.
    LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).                                                                                                         
    # PIN            = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
       
    
    # A = [13, 14, 15, 16, 23, 26, 32, 33, 36, 37, 42, 47, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 67, 68, 71, 78, 81, 88]
    # B = [13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 57, 52, 62,  67, 72, 77, 82, 83, 84, 85, 86]
    # C = [13, 14, 15, 16, 22, 27, 38, 41, 58, 61, 72, 77, 83, 84, 85, 86]
    # D = [14, 15, 16, 17, 22, 26, 32, 37, 42, 47, 52, 57, 62, 67, 73, 77, 82, 83, 84, 84, 85]
    # E = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 57, 62, 77, 82, 83, 84, 85, 86, 87]
    # F = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 47, 57, 62, 77, 82]
    # G = [13, 14, 15, 16, 17, 21, 27, 38, 41, 53, 54, 58, 61, 67, 72, 78, 81, 87, 93, 94, 95, 96, 97]
    # H = [12, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 52, 57, 62, 67, 72, 77, 82, 87]
    # I = [12, 13, 14, 15, 16, 17, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 82, 83, 84, 85, 86, 87]
    # J = [11, 12, 13, 14, 15, 16, 17, 25, 34, 45, 54, 62, 65, 74, 77, 82, 83, 84, 85]
    # K = [12, 13, 17, 22, 25, 26, 34, 35, 37, 42, 43, 56, 57, 62, 64, 65, 73, 74, 77, 82, 86, 87]
    # L = [18, 21, 38, 41, 58, 61, 78, 81, 82, 83, 84, 85, 86, 87]
    # M = [11, 12, 13, 16, 17, 18, 21, 22, 23, 26, 27, 28, 31, 33, 36, 38, 41, 43, 44, 45, 46, 48, 51, 54, 55, 58, 61, 68, 71, 78, 81, 88]
    # N = [11, 17, 18, 21, 22, 23, 28, 31, 36, 38, 41, 44, 48, 51, 54, 58, 61, 65, 66, 68, 71, 73, 78, 81, 87, 88]
    # O = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 68, 72, 77, 83, 84, 85, 86]
    # P = [12, 13, 14, 15, 16, 17, 22, 28, 31, 37, 42, 48, 52, 53, 54, 55, 56, 57, 62, 77, 82]
    # Q = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 66, 68, 72, 77, 83, 84, 85, 86, 88]
    # R = [12, 13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 55, 57, 62, 65, 73, 77, 82, 87]
    # S = [12, 13, 14, 15, 16, 17, 118, 21, 38, 41, 52, 53, 54, 55, 56, 57, 68, 71, 82, 83, 84, 85, 86, 87]
    # T = [11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
    # U = [11, 18, 21, 28, 31, 38, 41, 48, 51, 58, 61, 68, 71, 78, 82, 83, 84, 85, 86, 87]
    # V = [11, 18, 21, 28, 31, 38, 42, 47, 52, 57, 63, 66, 73, 76, 84, 85]
    # W = [11, 18, 21, 28, 31, 38, 41, 44, 45, 48, 51, 54, 55, 58, 61, 63, 66, 68, 71, 73, 76, 78, 82, 87]
    # X = [11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88]
    # Y = [11, 18, 21, 22, 27, 28, 32, 33, 36, 37, 43, 46, 54, 55, 64, 65, 74, 75, 84, 85]
    # Z = [11, 12, 13, 14, 15, 16, 17, 18, 28, 32, 33, 45, 55, 62, 63, 78, 81, 82, 83, 84, 85, 86, 87, 88]


    # letters = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
    #     'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
    #     'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}
    
        
    def __init__():
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        # ## for pin in buttonpins:
        # ## create a button with proper offset
        # # *************************NEED TO COMPLETE THIS*************************
        # button0 = new Button(0)
        # button1 = new Button(1)

    def display_letter(letter, color):
        for i in range(len(letter)):
            current_pixel = letter[i]
            strip.setPixelColor(current_pixel, color)
            strip.show() 

    def turn_off():
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()

    # Try
    # def __init__(offset, strip, pin):
    #     offset = offset * 100
    #     strip = strip
    #     pin = pin

    # def turn_on(current_pixel, color):
    #     strip.setPixelColor(current_pixel + offset, color)
    #     strip.show() 

    # def turn_off(current_pixel, color):
    #     strip.setPixelColor(current_pixel + offset, Color(0, 0, 0))

    # def display_letter(letter, color):
    #     # letter = 'A'
    #     lights = letters[letter]
    #     for light in lights:
    #         turn_on(light, color)
    
    
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
    
    
    
    
    def display_output(letter, is_correct):
    # might have to map in number to tiles_num by finding which index the pin is located at
        current_letter = [x + offset for x in letters[letter]]
        if (is_correct):
            display_letter(current_letter, Color(0, 250,0))
        else:
            display_letter(current_letter, Color(250, 0,0))

    # **************MAYBE ATTEMPT TO SIMPLIFY THIS (would this go in config.py??)*******************
    def initialize_letter(randomizedLetters):
        current_tile = 0
        for letter in randomizedLetters:
            current_tile += 1
            if current_tile == 1:
                current_letter = light.letter_arrays[letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 2:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 100 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 3:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 200 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 4:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 300 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 5:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 400 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 6:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 500 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 7:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 600 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150))
            elif current_tile == 8:
                current_letter = light.letter_arrays[letter]
                current_letter = [x + 700 for x in current_letter]
                display_letter(current_letter, Color(150, 150,150)) 
    
    
    
    # ************************CHECK TO SEE IF THE FINAL ONE WILL REPLACE THE TOP TWO*************
    # This function displays if the input was correct
    def correct_light(letter, pin):
        # might have to map in number to tiles_num by finding which index the pin is located at
        tiles_num = BUTTON_PINS.index(pin)
        addition = tiles_num * 100

        current_letter = light.letter_arrays[letter]
        current_letter = [x + addition for x in current_letter]
        display_letter(current_letter, Color(0, 250,0))


    # This function displays if the input was incorrect
    def wrong_light(letter, pin):
        # might have to map in number to tiles_num by finding which index the pin is located at
        tiles_num = BUTTON_PINS.index(pin)
        addition = tiles_num * 100
        current_letter = light.letter_arrays[letter]
        current_letter = [x + addition for x in current_letter]
        display_letter(current_letter, Color(250, 0,0))

    # # Replaces the functions above - Levi's quick attempt
    # def display_output(letter, pin, is_correct):
    #     tiles_num = BUTTON_PINS.index(pin)
    #     addition = tiles_num * 100
    #     current_letter = light.letter_arrays[letter]
    #     current_letter = [x + addition for x in current_letter]
    #     if (is_correct):
    #         display_letter(current_letter, Color(0, 250,0))
    #     else:
    #         display_letter(current_letter, Color(250, 0,0))