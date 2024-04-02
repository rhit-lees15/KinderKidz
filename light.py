#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 100      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 65     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53



# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def display_A(color):
        A = [13, 14, 15, 16, 23, 26, 32, 33, 36, 37, 42, 47, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 67, 68, 71, 78, 81, 88]
        for i in range(len(A)):
            strip.setPixelColor(i, color)
            strip.show() 
            # time.sleep(50/1000.0)
       
def display_B(color):
        B = [13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 56, 52, 57, 62,  67, 72, 77, 82, 83, 84, 85, 86]
        for i in range(len(B)):
            strip.setPixelColor(i, color)
            strip.show()        

def display_C(color):
        C = [13, 14, 15, 16, 22, 27, 31, 38, 41, 51, 61, 68, 72, 77, 83, 84, 85, 86]
        for i in range(len(C)):
            strip.setPixelColor(i, color)
            strip.show()        

def display_D(color):
        D = [14, 15, 16, 17, 22, 26, 32, 37, 42, 47, 52, 57, 62, 67, 73, 77, 82, 83, 84, 84]
        for i in range(len(D)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_E(color):
        E = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 57, 62, 77, 82, 83, 84, 85, 86, 87]
        for i in range(len(E)):
            strip.setPixelColor(i, color)
            strip.show() 
      
def display_F(color):
        F = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 47, 57, 62, 77, 82]
        for i in range(len(F)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_G(color):
        F = [13, 14, 15, 16, 17, 21, 27, 38, 41, 53, 54, 58, 61, 67, 72, 78, 81, 87, 93, 94, 95, 96, 97]
        for i in range(len(F)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_H(color):
        H = [12, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 52, 57, 62, 67, 72, 77, 82, 87]
        for i in range(len(H)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_I(color):
        I = [12, 13, 14, 15, 16, 17, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 82, 83, 84, 85, 86, 87]
        for i in range(len(I)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_J(color):
        J = [11, 12, 13, 14, 15, 16, 17, 25, 34, 45, 54, 62, 65, 74, 77, 82, 83, 84, 85]
        for i in range(len(J)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_K(color):
        K = [12, 13, 17, 22, 25, 26, 34, 35, 37, 42, 43, 56, 57, 62, 64, 65, 73, 74, 77, 82, 86, 87]
        for i in range(len(K)):
            strip.setPixelColor(i, color)
            strip.show()

def display_L(color):
        L = [18, 21, 38, 41, 58, 61, 78, 81, 82, 83, 84, 85, 86, 87]
        for i in range(len(L)):
            strip.setPixelColor(i, color)
            strip.show()

def display_M(color):
        M = [11, 12, 13, 16, 17, 18, 21, 22, 23, 26, 27, 28, 31, 33, 36, 38, 41, 43, 44, 45, 46, 48, 51, 54, 55, 58, 61, 68, 71, 78, 81, 88]
        for i in range(len(M)):
            strip.setPixelColor(i, color)
            strip.show() 

def display_N(color):
        N = [11, 17, 18, 21, 22, 23, 28, 31, 36, 38, 41, 44, 48, 51, 54, 58, 61, 65, 66, 68, 71, 73, 78, 81, 87, 88]
        for i in range(len(N)):
            strip.setPixelColor(i, color)
            strip.show()

def display_O(color):
        O = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 68, 72, 77, 83, 84, 85, 86]
        for i in range(len(O)):
            strip.setPixelColor(i, color)
            strip.show()

def display_P(color):
        P = [12, 13, 14, 15, 16, 17, 22, 28, 31, 37, 42, 48, 52, 53, 54, 55, 56, 57, 62, 77, 82]
        for i in range(len(P)):
            strip.setPixelColor(i, color)
            strip.show()  

def display_Q(color):
        Q = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 66, 68, 72, 77, 83, 84, 85, 86, 88]
        for i in range(len(Q)):
            strip.setPixelColor(i, color)
            strip.show()  

def display_R(color):
        Q = [12, 13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 55, 57, 62, 65, 73, 77, 82, 87]
        for i in range(len(Q)):
            strip.setPixelColor(i, color)
            strip.show()

def display_S(color):
        S = [11, 12, 13, 14, 15, 16, 17, 118, 21, 38, 41, 51, 52, 53, 54, 55, 56, 57, 58, 68, 71, 81, 82, 83, 84, 85, 86, 87, 88]
        for i in range(len(S)):
            strip.setPixelColor(i, color)
            strip.show()  

def display_T(color):
        T = [11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
        for i in range(len(T)):
            strip.setPixelColor(i, color)
            strip.show()

def display_U(color):
        U = [11, 18, 21, 28, 31, 38, 41, 48, 51, 58, 61, 68, 71, 78, 82, 83, 84, 85, 86, 87]
        for i in range(len(U)):
            strip.setPixelColor(i, color)
            strip.show()

def display_V(color):
        P = [11, 18, 21, 28, 31, 38, 42, 47, 52, 57, 63, 66, 73, 76, 84, 85]
        for i in range(len(P)):
            strip.setPixelColor(i, color)
            strip.show()

def display_W(color):
        W = [11, 18, 21, 28, 31, 38, 41, 44, 45, 48, 51, 54, 55, 58, 61, 63, 66, 68, 71, 73, 76, 78, 82, 87]
        for i in range(len(W)):
            strip.setPixelColor(i, color)
            strip.show()

def display_X(color):
        X = [11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88]
        for i in range(len(X)):
            strip.setPixelColor(i, color)
            strip.show()  

def display_Y(color):
        Y = [11, 18, 21, 22, 27, 28, 32, 33, 36, 37, 43, 46, 54, 55, 64, 65, 74, 75, 84, 85]
        for i in range(len(Y)):
            strip.setPixelColor(i, color)
            strip.show()  

def display_Z(color):
        Z = [11, 12, 13, 14, 15, 16, 17, 18, 28, 32, 33, 45, 55, 62, 63, 78, 81, 82, 83, 84, 85, 86, 87, 88]
        for i in range(len(Z)):
            strip.setPixelColor(i, color)
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

        while True:
            display_C(Color(255,0,0))
            # display_A(Color(255,0,0))
            # display_T(Color(255,0,0))

            
            # print ('Color wipe animations.')
            # colorWipe(strip, Color(255, 0, 0))  # Red wipe
            # colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            # colorWipe(strip, Color(0, 0, 255))  # Green wipe
#             print ('Theater chase animations.')
#             theaterChase(strip, Color(127, 127, 127))  # White theater chase
#             theaterChase(strip, Color(127,   0,   0))  # Red theater chase
#             theaterChase(strip, Color(  0,   0, 127))  # Blue theater chase
#             print ('Rainbow animations.')
#             rainbow(strip)
#             rainbowCycle(strip)
#             theaterChaseRainbow(strip)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
