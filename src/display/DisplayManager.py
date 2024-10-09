from pygame import Color
from config import letters
from Button import Button

# import letters from config
# import Button from Button

class DisplayManager:

    LED_COUNT      = 800      # Number of LED pixels.
    LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).                                                                                                         
    PIN            = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 5     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

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