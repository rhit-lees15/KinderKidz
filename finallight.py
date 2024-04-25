#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
import randomLetters
from pygame import Color
from rpi_ws281x import *
import argparse
import RPi.GPIO as GPIO

# LED strip configuration:
LED_COUNT      = 300      # Number of LED pixels.
LED_PIN        = 18  # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 65     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']

BUTTON_PIN = 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.input(BUTTON_PIN)

A = [13, 14, 15, 16, 23, 26, 32, 33, 36, 37, 42, 47, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 67, 68, 71, 78, 81, 88]
B = [13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 56, 52, 57, 62,  67, 72, 77, 82, 83, 84, 85, 86]
C = [13, 14, 15, 16, 22, 27, 38, 41, 58, 61, 72, 77, 83, 84, 85, 86]
D = [14, 15, 16, 17, 22, 26, 32, 37, 42, 47, 52, 57, 62, 67, 73, 77, 82, 83, 84, 84]
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
S = [11, 12, 13, 14, 15, 16, 17, 118, 21, 38, 41, 51, 52, 53, 54, 55, 56, 57, 58, 68, 71, 81, 82, 83, 84, 85, 86, 87, 88]
T = [11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
U = [11, 18, 21, 28, 31, 38, 41, 48, 51, 58, 61, 68, 71, 78, 82, 83, 84, 85, 86, 87]
V = [11, 18, 21, 28, 31, 38, 42, 47, 52, 57, 63, 66, 73, 76, 84, 85]
W = [11, 18, 21, 28, 31, 38, 41, 44, 45, 48, 51, 54, 55, 58, 61, 63, 66, 68, 71, 73, 76, 78, 82, 87]
X = [11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88]
Y = [11, 18, 21, 22, 27, 28, 32, 33, 36, 37, 43, 46, 54, 55, 64, 65, 74, 75, 84, 85]
Z = [11, 12, 13, 14, 15, 16, 17, 18, 28, 32, 33, 45, 55, 62, 63, 78, 81, 82, 83, 84, 85, 86, 87, 88]


letter_arrays = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
    'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
    'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}

def turn_off():
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

def display_letter(letter, color):
    for i in range(len(letter)):
        current_pixel = letter[i]
        strip.setPixelColor(current_pixel, color)
        strip.show()  
        strip.setPixelColor(current_pixel, color)
        strip.show()  


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:
        word = randomLetters.generateRandomWord(wordList)
        print(word)
        letters = list(word)
        current_index = 0

        while True:
            for letter in letters:
                if current_index == 1:
                    current_letter = letter_arrays[letter]
                    display_letter(current_letter, Color(150, 150,150))
                elif current_index == 2:
                    current_letter = letter_arrays[letter]
                    current_letter = [[num + 100 for num in row] for row in current_letter]
                    display_letter(current_letter, Color(150, 150,150))

                elif current_index ==3:
                    current_letter = letter_arrays[letter]
                    current_letter = [[num + 200 for num in row] for row in current_letter]

                    display_letter(current_letter, Color(150, 150,150))


                while True:
                    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
                        print("here")
                        break
                    # time.sleep(0.1)
                turn_off()
                time.sleep(800/1000)



    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
