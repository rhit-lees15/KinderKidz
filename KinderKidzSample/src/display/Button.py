
# Display LEDS, and respond when pushed
import letters from config

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



    
