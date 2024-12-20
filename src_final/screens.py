import sys
import pygame
import random
from sound import *

import tkinter as tk

# Full screen the GUI to fill the screen
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Screen dimensions
screen_width, screen_height = display.get_size()
screen = pygame.display.set_mode((screen_width, screen_height))

# image_bg = pygame.image.load("ANIMALS.png")
# image_bg_top = screen_height - image_bg.get_height()
# image_bg_left = screen_width/2 - image_bg.get_width()/2

# screen.blit(image_bg, (image_bg_left,image_bg_top))

class MainScreen:
    # def __init__(self, game):
    #     self.game = game

    #     # Button setup
    #     self.font = pygame.font.Font(None, 50)
    #     self.start_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 - 50, 200, 100)
    #     self.quit_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height - 120, 200, 80)

 ################### THIS IS A TEST TO SEE IF NEW CHANGES ARE SAVED #####################
    def __init__(self, game):
        self.game = game
    
        # Button setup
        self.font = pygame.font.Font(None, 50)
        
        # Load background image and scale it to fit the screen size
        self.background_image = pygame.image.load("/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/ANIMALS.png")
        self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
       
        # Centered Start/Quit buttons
        self.start_button = pygame.Rect(0, 0, 200, 100)
        self.start_button.center = (screen_width // 2, screen_height // 2 - 75)
       
        self.quit_button = pygame.Rect(0, 0, 200, 80)
        self.quit_button.center = (screen_width // 2, screen_height // 2 + 75)
        
        # # Centered Start/Quit buttons
        # self.start_button = pygame.Rect(0, 0, 200, 100)
        # self.start_button.center = (self.screen_width // 2, self.screen_height // 2 - 75)
       
        # self.quit_button = pygame.Rect(0, 0, 200, 80)
        # self.quit_button.center = (self.screen_width // 2, self.screen_height // 2 + 75)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.start_button.collidepoint(mouse_pos):
                # Switch to the Timer screen
                self.game.switch_screen(TimerScreen)
            elif self.quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    # def draw(self, screen):
    #     # Draw Start button
    #     pygame.draw.rect(screen, (0, 255, 0), self.start_button)
    #     start_text = self.font.render("Start", True, (255, 255, 255))
    #     screen.blit(start_text, (self.start_button.x + 50, self.start_button.y + 25))

    #     # Draw Quit button
    #     pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
    #     quit_text = self.font.render("Quit", True, (255, 255, 255))
    #     screen.blit(quit_text, (self.quit_button.x + 50, self.quit_button.y + 25))

    def draw(self, screen):
        # Draw the background image
        screen.blit(self.background_image, (0, 0))
        
        # Draw Start button
        pygame.draw.rect(screen, (0, 255, 0), self.start_button)
        start_text = self.font.render("Start", True, (255, 255, 255))
       
        # Center text within button
        start_text_rect = start_text.get_rect(center = self.start_button.center)
        screen.blit(start_text, start_text_rect)
 
        # Draw Quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
       
        # Center text within button
        quit_text_rect = quit_text.get_rect(center = self.quit_button.center)
        screen.blit(quit_text, quit_text_rect)

class TimerScreen:
    def __init__(self, game):
        # self.game = game
        # self.font = pygame.font.Font(None, 50)

        # # Button setup for 1 minute, 3 minutes, 5 minutes
        # self.two_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 - 100, 200, 60)
        # self.three_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2, 200, 60)
        # self.five_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 + 100, 200, 60)

        # self.add_word_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 + 180, 200, 60)

        self.game = game
        self.font = pygame.font.Font(None, 50)

        # Space between each button, width, and height
        button_spacing, button_width, button_height = 20, 250, 50
        
        # pygame.Rect(x, y, width, height)
        # Button setup for 1 minute, 3 minutes, 5 minutes
        self.two_min_button = pygame.Rect((screen_width - button_width) // 2, 
                                          ((1/4) * screen_height) // 2,
                                          button_width, button_height)
        self.three_min_button = pygame.Rect(self.two_min_button.x,
                                            self.two_min_button.y + button_height + button_spacing,
                                            button_width, button_height)
        self.five_min_button = pygame.Rect(self.three_min_button.x,
                                           self.three_min_button.y + button_height + button_spacing, 
                                           button_width, button_height)
        
        self.add_word_button = pygame.Rect(0, 0, 250, 80)
        self.add_word_button.center = (screen_width // 2, screen_height // 2 + 75)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.add_word_button.collidepoint(mouse_pos):
                self.game.switch_screen(AddWordScreen) 
            elif self.two_min_button.collidepoint(mouse_pos):
                print("2-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 120))
            elif self.three_min_button.collidepoint(mouse_pos):
                print("3.5-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 210))
            elif self.five_min_button.collidepoint(mouse_pos):
                print("5-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 300))

    def update(self):
        pass

    def draw(self, screen):
        # Draw the 1 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.two_min_button)
        two_min_text = self.font.render("2 Minutes", True, (255, 255, 255))
        two_min_text_rect = two_min_text.get_rect(center=self.two_min_button.center)
        screen.blit(two_min_text, two_min_text_rect)

        # Draw the 3 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.three_min_button)
        three_min_text = self.font.render("3.5 Minutes", True, (255, 255, 255))
        three_min_text_rect = three_min_text.get_rect(center=self.three_min_button.center)
        screen.blit(three_min_text, three_min_text_rect)

        # Draw the 5 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.five_min_button)
        five_min_text = self.font.render("5 Minutes", True, (255, 255, 255))
        five_min_text_rect = five_min_text.get_rect(center=self.five_min_button.center)
        screen.blit(five_min_text, five_min_text_rect)

        # Draw the Add Word button
        pygame.draw.rect(screen, (0, 255, 0), self.add_word_button)
        add_word_text = self.font.render("Add Words!", True, (255, 255, 255))
        add_word_text_rect = add_word_text.get_rect(center=self.add_word_button.center)
        screen.blit(add_word_text, add_word_text_rect)

from play import GameLogic
from buttons import Buttons
import RPi.GPIO as GPIO
import time
# Define GPIO pins for buttons
# BUTTON_PINS = [24, 25, 23, 22, 5, 6, 13, 12]
BUTTON_PINS = {24:0, 25:1, 23:2, 22:3, 5:4, 6:5, 13:6, 12:7}
DEBOUNCE_TIME = 2

class GameScreen:
    last_press_times = {}

    def __init__(self, game, game_duration):
        self.game = game
        self.game_duration = game_duration  # Time in seconds
        self.font = pygame.font.Font(None, 50)
        self.word_font = pygame.font.Font(None, 250)
 
        self.logic = GameLogic()
        self.current_word = self.logic.get_new_word()
        self.letter_map = self.logic.generate_buttons()

        # Timer setup
        self.start_time = pygame.time.get_ticks()

        # Quit button setup
        self.quit_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height - 120, 200, 80)

       # Initialize GPIO for buttons
        GPIO.setmode(GPIO.BCM)
        for pin in BUTTON_PINS.keys():
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.add_event_detect(pin, GPIO.FALLING, callback=self.gpio_button_pressed, bouncetime=500)
            GameScreen.last_press_times[pin] = 0 

    def gpio_button_pressed(self, pin):
        """Handles the event when a GPIO button is pressed with debounce protection."""
        current_time = time.time()  # Get the current time
        last_press_time = GameScreen.last_press_times.get(pin, 0)  # Get the last press time for this pin

        # Check if enough time has passed since the last press
        if current_time - last_press_time >= DEBOUNCE_TIME:
            GameScreen.last_press_times[pin] = current_time  # Update last press time
            button_number = BUTTON_PINS[pin]
            self.process_input(button_number)

        # """Handles the event when a GPIO button is pressed."""
        # button_number = BUTTON_PINS[pin]
        # self.process_input(button_number)
    
    def process_input(self, button_number):
        """Handles the logic for when a GPIO button (0-7) is pressed."""
        correct, message = self.logic.check_input(button_number)
        print(message)  # Print the result ("Correct", "Try again", "Next word")

        if message == "Next word":
            # Get new word and refresh buttons
            self.current_word = self.logic.get_new_word()
            self.letter_map = self.logic.generate_buttons()


    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            # Check if number keys 1 to 8 are pressed
            if event.key == pygame.K_1:
                self.process_input(1)
            elif event.key == pygame.K_2:
                self.process_input(2)
            elif event.key == pygame.K_3:
                self.process_input(3)
            elif event.key == pygame.K_4:
                self.process_input(4)
            elif event.key == pygame.K_5:
                self.process_input(5)
            elif event.key == pygame.K_6:
                self.process_input(6)
            elif event.key == pygame.K_7:
                self.process_input(7)
            elif event.key == pygame.K_0:
                self.process_input(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.quit_button.collidepoint(mouse_pos):
                pygame.quit()
                GPIO.cleanup()
                sys.exit()

    def update(self):
        # Calculate remaining time in seconds
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        self.remaining_time = self.game_duration - elapsed_time

        # End the game when the timer reaches zero
        if self.remaining_time <= 0:
            try:
                # pygame.mixer.music.unload()
                pygame.mixer.stop()
                pygame.mixer.music.stop()
                for pin in BUTTON_PINS.keys():
                    GPIO.remove_event_detect(pin)
                time.sleep(0.1)
                # GPIO.cleanup()
                # pygame.mixer.quit()
                # pygame.quit()
                self.game.switch_screen(lambda game: MusicScreen(game))
                # # Load background image and scale it to fit the screen size
                # self.background_image = pygame.image.load("src_final/ANIMALS.png")
                # self.background_image = pygame.transform.scale(self.background_image, (screen_width, screen_height))
            except Exception as e:
                print(f"Error during GPIO cleanup or transition: {e}")
            return

        # Calculate minutes and seconds from remaining time
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        time_display = f"{minutes:02}:{seconds:02}"  # Format as mm:ss

        # Display the timer on the screen
        font = pygame.font.Font(None, 36)  # Choose font and size
        timer_text = font.render(time_display, True, (255, 255, 255))  # White color
        screen = pygame.display.get_surface()  # Get the screen surface
        screen.blit(timer_text, (screen.get_width() // 2 - timer_text.get_width() // 2, 20))  # Centered at the top

    # def update(self):
    #     # Calculate remaining time
    #     elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
    #     self.remaining_time = self.game_duration - elapsed_time

    #     # End the game when the timer reaches zero
    #     if self.remaining_time <= 0:
    #         self.game.switch_screen(lambda game: MusicScreen(game))

    def draw(self, screen):
        # # Draw the remaining time (top-right corner)
        # time_text = self.font.render(f"Time: {self.remaining_time}", True, (255, 255, 255))
        # screen.blit(time_text, (self.game.screen_width - 150, 20))

        # # Draw the random word (center of the screen)
        # word_text = self.font.render(self.current_word, True, (255, 255, 255))
        # screen.blit(word_text, (self.game.screen_width // 2, self.game.screen_height // 2))
    
        word_text = self.word_font.render(self.current_word, True, (255, 255, 255))
        word_rect = word_text.get_rect(center=(screen_width // 2, screen_height // 3))
        screen.blit(word_text, word_rect)

        # # Display the letter-to-button mapping for the user's reference
        # for i in range(8):
        #     letter = self.letter_map[i + 1]
        #     button_text = self.font.render(f"{i + 1}: {letter}", True, (255, 255, 255))
        #     screen.blit(button_text, (self.game.screen_width // 2 - 200 + (i % 4) * 150, 300 + (i // 4) * 50))

        # Draw the quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=self.quit_button.center)  # Centered in the quit button
        screen.blit(quit_text, quit_rect)

    def __del__(self):
        GPIO.cleanup()
        # pygame.mixer.quit()
        # pygame.quit()

import webbrowser
from pygame import mixer
import platform
from pygame import Color


from led import LED

class MusicScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)
        self.led = LED()

        pygame.mixer.init()
        # mixer.init()  # Initialize the mixer for playing audio
        mixer.music.set_volume(0.2)

        Audio.play_dance_break()
        print("Song is about to play - clear led")
        self.led.clear_all()

        # Buttons setup for songs
        self.song_buttons = []
        self.songs = [
            "/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/Audio/Songs/twinkle-twinkle.mp3", # Twinkle
            "/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/Audio/Songs/happy-and-you-know-it.mp3", # Happy
            # "Audio/Songs/idk.mp3",
            "/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/Audio/Songs/my-year-zombies.mp3", # My Year
            "/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/Audio/Songs/puff-the-magic-dragon.mp3", # Puff
            "/home/kinderkidz/Capstone/KinderKidz - Fall/KinderKidz/src_final/Audio/Songs/body-bop-bop.mp3" # Body Bop
        ]
        # self.song_labels = [f"Song {i+1}" for i in range(5)]
        self.song_labels = ["Twinkle", "Happy", "My Year", "Puff", "Body Bop"]

        # Calculate column and row placement
        for i in range(len(self.songs)):
            column = i % 2  # Determines left or right column
            row = i // 2    # Row index, increments every 2 songs
            x_position = game.screen_width // 3 + column * (game.screen_width // 2 - 100)  # Left or right column position
            y_position = 50 + row * 60  # Increment row position

            # Create button at calculated position and add to list
            button = pygame.Rect(x_position - 100, y_position, 200, 50)
            self.song_buttons.append(button)

        # "Choose Your Own!" button
        self.choose_button = pygame.Rect(game.screen_width - 250, game.screen_height - 80, 200, 50)

        # "Back to the game!" button
        self.back_button = pygame.Rect(50, game.screen_height - 80, 200, 50)

        # Quit button setup
        self.quit_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height - 120, 200, 80)


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Check if a song button is clicked
            for i, button in enumerate(self.song_buttons):
                if button.collidepoint(mouse_pos):
                    mixer.music.load(self.songs[i])
                    # mixer.music.set_volume(0.3)

                    mixer.music.set_volume(0.7)
                    mixer.music.play()
                    self.led.theaterChase(Color(127, 127, 127))  # White theater chase
                    self.led.theaterChase(Color(127,   0,   0))  # Red theater chase
                    self.led.theaterChase(Color(  0,   0, 127))  # Blue theater chase
                    # print ('Rainbow animations.')
                    # self.led.rainbow()
                    # self.led.rainbowCycle()
        #             theaterChaseRainbow(strip)

            # Check if "Choose Your Own!" is clicked
            if self.choose_button.collidepoint(mouse_pos):
                print("Button pressed!!!!!")
                try:
                    # Forcing Chromium browser on Raspberry Pi
                    webbrowser.get("chromium-browser --no-sandbox %s").open("https://www.youtube.com/")
                except Exception as e:
                    print(f"Error opening web browser: {e}")
                # webbrowser.open("https://www.youtube.com/")
                # self.open_youtube()

            # Check if "Back to the game!" is clicked
            if self.back_button.collidepoint(mouse_pos):
                mixer.music.stop()
                self.game.switch_screen(lambda game: TimerScreen(game))


            # Check if the quit button is clicked
            if self.quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self, screen):
        for i, button in enumerate(self.song_buttons):
            # Draw the button rectangle
            pygame.draw.rect(self.game.screen, (0, 255, 0), button)  # Green color for song buttons

            # Render the text for the song label
            label_surface = self.font.render(self.song_labels[i], True, (255, 255, 255))  # White text
            label_rect = label_surface.get_rect(center=button.center)  # Center the text in the button

            # Draw the text on the screen
            self.game.screen.blit(label_surface, label_rect)
            
        # Draw the "Choose Your Own!" button
        pygame.draw.rect(screen, (0, 255, 255), self.choose_button)
        choose_text = self.font.render("Other Songs", True, (255, 255, 255))
        choose_rect = choose_text.get_rect(center=self.choose_button.center)  # Centered in the "Choose Your Own!" button
        screen.blit(choose_text, choose_rect)
        
        # Draw the "Back to the game!" button
        pygame.draw.rect(screen, (255, 165, 0), self.back_button)
        back_text = self.font.render("Home", True, (255, 255, 255))
        back_rect = back_text.get_rect(center=self.back_button.center)  # Centered in the "Back to the game!" button
        screen.blit(back_text, back_rect)

        # Draw the quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        quit_rect = quit_text.get_rect(center=self.quit_button.center)  # Centered in the quit button
        screen.blit(quit_text, quit_rect)
    # def draw(self, screen):
    #     for i, button in enumerate(self.song_buttons):
    #         # Draw the button rectangle
    #         pygame.draw.rect(self.game.screen, (0, 255, 0), button)  # Green color for song buttons

    #         # Render the text for the song label
    #         label_surface = self.font.render(self.song_labels[i], True, (255, 255, 255))  # White text
    #         label_rect = label_surface.get_rect(center=button.center)  # Center the text in the button

    #         # Draw the text on the screen
    #         self.game.screen.blit(label_surface, label_rect)
            
    #     # Draw the "Choose Your Own!" button
    #     pygame.draw.rect(screen, (0, 255, 255), self.choose_button)
    #     choose_text = self.font.render("Other Songs", True, (255, 255, 255))
    #     choose_rect = choose_text.get_rect(center=self.choose_button.center)  # Centered in the "Choose Your Own!" button
    #     screen.blit(choose_text, choose_rect)
        
    #     # Draw the "Back to the game!" button
    #     pygame.draw.rect(screen, (255, 165, 0), self.back_button)
    #     back_text = self.font.render("Home", True, (255, 255, 255))
    #     back_rect = back_text.get_rect(center=self.back_button.center)  # Centered in the "Back to the game!" button
    #     screen.blit(back_text, back_rect)

    #     # Draw the quit button
    #     pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
    #     quit_text = self.font.render("Quit", True, (255, 255, 255))
    #     quit_rect = quit_text.get_rect(center=self.quit_button.center)  # Centered in the quit button
    #     screen.blit(quit_text, quit_rect)

    # def draw(self, screen):
    #     # Draw the song buttons
    #     for i, button in enumerate(self.song_buttons):
    #         pygame.draw.rect(screen, (0, 255, 0), button)
    #         song_text = self.font.render(self.song_labels[i], True, (255, 255, 255))
    #         screen.blit(song_text, (button.x + 50, button.y + 10))

    #     # Draw the "Choose Your Own!" button
    #     pygame.draw.rect(screen, (0, 255, 255), self.choose_button)
    #     choose_text = self.font.render("Choose Song!", True, (255, 255, 255))
    #     screen.blit(choose_text, (self.choose_button.x + 20, self.choose_button.y + 10))
        
    #     # Draw the "Back to the game!" button
    #     pygame.draw.rect(screen, (255, 165, 0), self.back_button)
    #     back_text = self.font.render("Home", True, (255, 255, 255))
    #     screen.blit(back_text, (self.back_button.x + 20, self.back_button.y + 10))

    #     # Draw the quit button
    #     pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
    #     quit_text = self.font.render("Quit", True, (255, 255, 255))
    #     screen.blit(quit_text, (self.quit_button.x + 50, self.quit_button.y + 25))

class AddWordScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)
        
        # Centered at the bottom
        # self.add_word_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 + 180, 200, 60)
        self.add_word_button = pygame.Rect(0, 0, 150, 50) # was (0, 0, 200, 80)
        self.add_word_button.center = (screen_width // 2, screen_height // 2 + 120) # was + 75

        # Centered at the top
        self.home_button = pygame.Rect((game.screen_width - 150) // 2, 10, 150, 50)
        # self.home_button = pygame.Rect(0, 0, 150, 50)
        # self.home_button.center = (screen_width // 2, screen_height - 150)

        self.input_box = pygame.Rect(100, 100, 600, 50)
        self.input_text = ''
        self.word_list = GameLogic.get_word_list()
        
        # Scroll position for the word list
        self.scroll_y = 0
        self.scroll_speed = 40  # How much to scroll with each mouse wheel movement
        self.word_height = 40  # Height of each word in the list
        self.scroll_bar = pygame.Rect(game.screen_width - 20, 200, 10, 100)  # Scroll bar dimensions

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.add_word_button.collidepoint(mouse_pos):
                # Add word screen logic (refresh or reset screen)
                self.game.switch_screen(lambda game: AddWordScreen(game))
            elif self.home_button.collidepoint(mouse_pos):
                # Return to Home
                self.game.switch_screen(lambda game: TimerScreen(game))

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.input_text:
                    GameLogic.add_word(self.input_text)  # Add the word to the list
                    print("Word Added!")
                    self.word_list = GameLogic.get_word_list()
                    self.input_text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

        elif event.type == pygame.MOUSEWHEEL:
            # Adjust scroll position based on mouse wheel input
            self.scroll_y += event.y * self.scroll_speed  # Adjust scroll speed as needed

            # Prevent scrolling beyond the bounds of the word list
            max_scroll = max(0, -(len(self.word_list) * self.word_height - (self.game.screen_height - 250)))
            self.scroll_y = max(min(self.scroll_y, 0), max_scroll)

    def update(self):
        # Update scroll bar position based on scroll_y
        # visible_height = self.game.screen_height - 250  # Height for the word list display
        # content_height = len(self.word_list) * 40
        # if content_height > visible_height:
        #     self.scroll_bar.height = max(50, visible_height * visible_height // content_height)
        #     scroll_ratio = -self.scroll_y / max(1, content_height - visible_height)
        #     self.scroll_bar.y = 200 + int(scroll_ratio * (visible_height - self.scroll_bar.height))
        pass

    def draw(self, screen):
        # # Draw the Add Word button
        # pygame.draw.rect(screen, (0, 255, 0), self.add_word_button)
        # add_word_text = self.font.render("Add", True, (255, 255, 255))
        # screen.blit(add_word_text, (self.add_word_button.x + 25, self.add_word_button.y + 15))
        
        # Draw Add button
        pygame.draw.rect(screen, (0, 255, 0), self.add_word_button)
        add_word_text = self.font.render("Add", True, (255, 255, 255))
       
        # Center text within button
        add_word_text_rect = add_word_text.get_rect(center = self.add_word_button.center)
        screen.blit(add_word_text, add_word_text_rect)

        # Draw the input box
        pygame.draw.rect(screen, (255, 255, 255), self.input_box, 2)
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        screen.blit(text_surface, (self.input_box.x + 5, self.input_box.y + 5))

        # # Draw the current word list with scrolling
        # y_position = 200 + self.scroll_y  # Apply scroll offset here
        # max_height = screen.get_height() - 250  # Leave space for buttons and input box

        # for word in self.word_list:
        #     word_surface = self.font.render(word, True, (255, 255, 255))
        #     screen.blit(word_surface, (100, y_position))
        #     y_position += self.word_height  # Adjust y_position for each word

        # # Draw the scroll bar
        # pygame.draw.rect(screen, (180, 180, 180), self.scroll_bar)  # Gray color for scroll bar

        # Constants for column layout
        column_width = 200  # Width allocated to each column
        max_columns = self.game.screen_width // column_width
        x_margin = 100  # Left margin for the first column
        y_start = 200 + self.scroll_y  # Apply scroll offset
        row_spacing = self.word_height  # Spacing between rows

        # Draw the current word list in columns
        for index, word in enumerate(self.word_list):
            column = index % max_columns  # Determine the column (0, 1, 2, ...)
            row = index // max_columns  # Determine the row (0, 1, 2, ...)
            x_position = x_margin + column * column_width
            y_position = y_start + row * row_spacing
            
            # Only render words within the visible screen area
            if 200 <= y_position <= screen.get_height() - 50:
                word_surface = self.font.render(word, True, (255, 255, 255))
                screen.blit(word_surface, (x_position, y_position))

        # Draw the "Return to Home" button
        pygame.draw.rect(screen, (255, 0, 0), self.home_button)
        home_text = self.font.render("Home", True, (255, 255, 255))
        home_text_rect = home_text.get_rect(center=self.home_button.center)
        screen.blit(home_text, home_text_rect)