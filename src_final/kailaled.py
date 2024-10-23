# led.py

import time
from pygame import Color
from rpi_ws281x import *
import argparse
from button import BUTTON_PINS


# LED strip configuration:
LED_COUNT      = 800     # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


A = [13, 14, 15, 16, 23, 26, 32, 33, 36, 37, 42, 47, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 67, 68, 71, 78, 81, 88]
B = [13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 57, 52, 62,  67, 72, 77, 82, 83, 84, 85, 86]
C = [13, 14, 15, 16, 22, 27, 38, 41, 58, 61, 72, 77, 83, 84, 85, 86]
D = [14, 15, 16, 17, 22, 26, 32, 37, 42, 47, 52, 57, 62, 67, 73, 77, 82, 83, 84, 84, 85]
E = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 57, 62, 77, 82, 83, 84, 85, 86, 87]
F = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 47, 57, 62, 77, 82]
G = [13, 14, 15, 16, 17, 21, 27, 38, 41, 53, 54, 58, 61, 67, 72, 78, 81, 87, 93, 94, 95, 96, 97]
H = [12, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 52, 57, 62, 67, 72, 77, 82, 87]
I = [12, 13, 14, 15, 16, 17, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 82, 83, 84, 85, 86, 87]
J = [11, 12, 13, 14, 15, 16, 17, 25, 34, 45, 54, 62, 65, 74, 77, 82, 83, 84, 85]
K = [12, 13, 17, 22, 25, 26, 34, 35, 37, 42, 43, 56, 57, 62, 64, 65, 73, 74, 77, 82, 86, 87]
L = [18, 21, 38, 41, 58, 61, 78, 81, 82, 83, 84, 85, 86, 87]
M = [11, 12, 13, 16, 17, 18, 21, 22, 23, 26, 27, 28, 31, 33, 36, 38, 41, 43, 44, 45, 46, 48, 51, 54, 55, 58, 61, 68, 71, 78, 81, 88]
N = [11, 17, 18, 21, 22, 23, 28, 31, 36, 38, 41, 44, 48, 51, 54, 58, 61, 65, 66, 68, 71, 73, 78, 81, 87, 88]
O = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 68, 72, 77, 83, 84, 85, 86]
P = [12, 13, 14, 15, 16, 17, 22, 28, 31, 37, 42, 48, 52, 53, 54, 55, 56, 57, 62, 77, 82]
Q = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 66, 68, 72, 77, 83, 84, 85, 86, 88]
R = [12, 13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 55, 57, 62, 65, 73, 77, 82, 87]
S = [12, 13, 14, 15, 16, 17, 18, 21, 38, 41, 52, 53, 54, 55, 56, 57, 68, 71, 82, 83, 84, 85, 86, 87]
T = [11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
U = [11, 18, 21, 28, 31, 38, 41, 48, 51, 58, 61, 68, 71, 78, 82, 83, 84, 85, 86, 87]
V = [11, 18, 21, 28, 31, 38, 42, 47, 52, 57, 63, 66, 73, 76, 84, 85]
W = [11, 18, 21, 28, 31, 38, 41, 44, 45, 48, 51, 54, 55, 58, 61, 63, 66, 68, 71, 73, 76, 78, 82, 87]
X = [11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88]
Y = [11, 18, 21, 22, 27, 28, 32, 33, 36, 37, 43, 46, 54, 55, 64, 65, 74, 75, 84, 85]
Z = [11, 12, 13, 14, 15, 16, 17, 18, 28, 32, 33, 45, 55, 62, 63, 78, 81, 82, 83, 84, 85, 86, 87, 88]


letters = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
        'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
        'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}

def display_letter(letter, color):
    for i in range(len(letter)):
        current_pixel = letter[i]
        strip.setPixelColor(current_pixel, color)
        strip.show()

def turn_off():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
        strip.show()
    
class LEDs:

    def __init__():
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

    def initialize_letter(randomizedLetters):
     current_tile = 0
     for letter in randomizedLetters:
        current_tile += 1
        if current_tile == 1:
            current_letter =letters[letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 2:
            current_letter =letters[letter]
            current_letter = [x + 100 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 3:
            current_letter =letters[letter]
            current_letter = [x + 200 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 4:
            current_letter =letters[letter]
            current_letter = [x + 300 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 5:
            current_letter =letters[letter]
            current_letter = [x + 400 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 6:
            current_letter =letters[letter]
            current_letter = [x + 500 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 7:
            current_letter =letters[letter]
            current_letter = [x + 600 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))
        elif current_tile == 8:
            current_letter =letters[letter]
            current_letter = [x + 700 for x in current_letter]
            display_letter(current_letter, Color(150, 150,150))

    def display_output(letter, pin, is_correct):
    # might have to map in number to tiles_num by finding which index the pin is located at
        tiles_num = BUTTON_PINS.index(pin)
        addition = tiles_num * 100
        current_letter = letters[letter]
        current_letter = [x + addition for x in current_letter]
        if (is_correct):
            display_letter(current_letter, Color(0, 250,0))
        else:
            display_letter(current_letter, Color(250, 0,0))

    

    



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def setup_and_run_leds():
    """Function to initialize and run LED animations."""
    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    try:
        # Run the LED animations
        print ('Running LED animations...')
        colorWipe(strip, Color(255, 0, 0))  # Red wipe
        colorWipe(strip, Color(0, 255, 0))  # Green wipe
        colorWipe(strip, Color(0, 0, 255))  # Blue wipe

    except KeyboardInterrupt:
        # Clear LEDs on exit
        colorWipe(strip, Color(0, 0, 0), 10)

# If running as standalone script, call the function
if __name__ == '__main__':
    setup_and_run_leds()


# import time

# from pygame import Color
# from rpi_ws281x import *
# import argparse

# # LED strip configuration:
# LED_COUNT      = 30     # Number of LED pixels.
# LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
# #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
# LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA        = 10      # DMA channel to use for generating a signal (try 10)
# LED_BRIGHTNESS = 65      # Set to 0 for darkest and 255 for brightest
# LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
# LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# # Define functions which animate LEDs in various ways.
# def colorWipe(strip, color, wait_ms=50):
#     """Wipe color across display a pixel at a time."""
#     for i in range(strip.numPixels()):
#         strip.setPixelColor(i, color)
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def theaterChase(strip, color, wait_ms=50, iterations=10):
#     """Movie theater light style chaser animation."""
#     for j in range(iterations):
#         for q in range(3):
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, color)
#             strip.show()
#             time.sleep(wait_ms/1000.0)
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, 0)

# def wheel(pos):
#     """Generate rainbow colors across 0-255 positions."""
#     if pos < 85:
#         return Color(pos * 3, 255 - pos * 3, 0)
#     elif pos < 170:
#         pos -= 85
#         return Color(255 - pos * 3, 0, pos * 3)
#     else:
#         pos -= 170
#         return Color(0, pos * 3, 255 - pos * 3)

# def rainbow(strip, wait_ms=20, iterations=1):
#     """Draw rainbow that fades across all pixels at once."""
#     for j in range(256*iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((i+j) & 255))
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def rainbowCycle(strip, wait_ms=20, iterations=5):
#     """Draw rainbow that uniformly distributes itself across all pixels."""
#     for j in range(256*iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
#         strip.show()
#         time.sleep(wait_ms/1000.0)

# def theaterChaseRainbow(strip, wait_ms=50):
#     """Rainbow movie theater light style chaser animation."""
#     for j in range(256):
#         for q in range(3):
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, wheel((i+j) % 255))
#             strip.show()
#             time.sleep(wait_ms/1000.0)
#             for i in range(0, strip.numPixels(), 3):
#                 strip.setPixelColor(i+q, 0)

# # Main program logic follows:
# if __name__ == '__main__':
#     # Process arguments
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
#     args = parser.parse_args()

#     # Create NeoPixel object with appropriate configuration.
#     strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
#     # Intialize the library (must be called once before other functions).
#     strip.begin()

#     print ('Press Ctrl-C to quit.')
#     if not args.clear:
#         print('Use "-c" argument to clear LEDs on exit')

#     try:

#         while True:
#             print ('Color wipe animations.')
#             colorWipe(strip, Color(255, 0, 0))  # Red wipe
#             colorWipe(strip, Color(0, 255, 0))  # Blue wipe
#             colorWipe(strip, Color(0, 0, 255))  # Green wipe
#             # print ('Theater chase animations.')
#             # theaterChase(strip, Color(127, 127, 127))  # White theater chase
#             # theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#             # theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#             # print ('Rainbow animations.')
#             # rainbow(strip)
#             # rainbowCycle(strip)
#             # theaterChaseRainbow(strip)

#     except KeyboardInterrupt:
#         if args.clear:
#             colorWipe(strip, Color(0,0,0), 10)