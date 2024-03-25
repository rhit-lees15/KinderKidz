import pygame
import os 

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


def playSound(filepath: str):
    # pygame.mixer.init()
    # my_sound = pygame.mixer.Sound(filepath)
    # my_sound.play()
    # pygame.time.wait(int(my_sound.get_length() * 1000))

    pygame.mixer.init()
    
    pygame.mixer.music.load(filepath)

    pygame.mixer.music.set_volume(0.7)

    pygame.mixer.music.play()

    
    while True: 
        print("Press 'p' to pause, 'r' to resume") 
        print("Press 'e' to exit the program") 
        query = input("  ") 
        
        if query == 'p': 
    
            # Pausing the music 
            pygame.mixer.music.pause()      
        elif query == 'r': 
    
            # Resuming the music 
            pygame.mixer.music.unpause() 
        elif query == 'e': 
    
            # Stop the mixer 
            pygame.mixer.music.stop() 
            break


def playOSSound(filepath:str):
    os.system(f"cvlc {filepath}")

    
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
    playOSSound('sample.wav')

    print ('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print ('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # Red wipe
            colorWipe(strip, Color(0, 255, 0))  # Blue wipe
            colorWipe(strip, Color(0, 0, 255))  # Green wipe


    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0,0,0), 10)
