import sys
import pygame
import random

class MainScreen:
    def __init__(self, game):
        self.game = game

        # Button setup
        self.font = pygame.font.Font(None, 50)
        self.start_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 - 50, 200, 100)
        self.quit_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height - 120, 200, 80)

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

    def draw(self, screen):
        # Draw Start button
        pygame.draw.rect(screen, (0, 255, 0), self.start_button)
        start_text = self.font.render("Start", True, (255, 255, 255))
        screen.blit(start_text, (self.start_button.x + 50, self.start_button.y + 25))

        # Draw Quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_text, (self.quit_button.x + 50, self.quit_button.y + 25))

class TimerScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)

        # Button setup for 1 minute, 3 minutes, 5 minutes
        self.one_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 - 100, 200, 60)
        self.three_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2, 200, 60)
        self.five_min_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height // 2 + 100, 200, 60)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.one_min_button.collidepoint(mouse_pos):
                print("1-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 10))
            elif self.three_min_button.collidepoint(mouse_pos):
                print("3-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 180))
            elif self.five_min_button.collidepoint(mouse_pos):
                print("5-minute timer selected!")
                self.game.switch_screen(lambda game: GameScreen(game, 300))

    def update(self):
        pass

    def draw(self, screen):
        # Draw the 1 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.one_min_button)
        one_min_text = self.font.render("10 Seconds", True, (255, 255, 255))
        screen.blit(one_min_text, (self.one_min_button.x + 25, self.one_min_button.y + 15))

        # Draw the 3 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.three_min_button)
        three_min_text = self.font.render("3 Minutes", True, (255, 255, 255))
        screen.blit(three_min_text, (self.three_min_button.x + 25, self.three_min_button.y + 15))

        # Draw the 5 minute button
        pygame.draw.rect(screen, (0, 255, 0), self.five_min_button)
        five_min_text = self.font.render("5 Minutes", True, (255, 255, 255))
        screen.blit(five_min_text, (self.five_min_button.x + 25, self.five_min_button.y + 15))

from play import GameLogic
class GameScreen:
    def __init__(self, game, game_duration):
        self.game = game
        self.game_duration = game_duration  # Time in seconds
        self.font = pygame.font.Font(None, 50)

 
        self.logic = GameLogic()
        self.current_word = self.logic.get_new_word()
        self.letter_map = self.logic.generate_buttons()


        # Timer setup
        self.start_time = pygame.time.get_ticks()

        # Quit button setup
        self.quit_button = pygame.Rect(game.screen_width // 2 - 100, game.screen_height - 120, 200, 80)

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
            elif event.key == pygame.K_8:
                self.process_input(8)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.quit_button.collidepoint(mouse_pos):
                pygame.quit()
                sys.exit()
    
    def process_input(self, button_number):
        """Handles the logic for when a number key (1-8) is pressed."""
        correct, message = self.logic.check_input(button_number)
        print(message)  # Print the result ("Correct", "Try again", "Next word")

        if message == "Next word":
            # Get new word and refresh buttons
            self.current_word = self.logic.get_new_word()
            self.letter_map = self.logic.generate_buttons()

    def update(self):
        # Calculate remaining time
        elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        self.remaining_time = self.game_duration - elapsed_time

        # End the game when the timer reaches zero
        if self.remaining_time <= 0:
            self.game.switch_screen(lambda game: MusicScreen(game))

    def draw(self, screen):
        # Draw the remaining time (top-right corner)
        time_text = self.font.render(f"Time: {self.remaining_time}", True, (255, 255, 255))
        screen.blit(time_text, (self.game.screen_width - 150, 20))

        # Draw the random word (center of the screen)
        word_text = self.font.render(self.current_word, True, (255, 255, 255))
        screen.blit(word_text, (self.game.screen_width // 2 - 50, self.game.screen_height // 2 - 25))

        # Display the letter-to-button mapping for the user's reference
        for i in range(8):
            letter = self.letter_map[i + 1]
            button_text = self.font.render(f"{i + 1}: {letter}", True, (255, 255, 255))
            screen.blit(button_text, (self.game.screen_width // 2 - 200 + (i % 4) * 150, 300 + (i // 4) * 50))

        # Draw the quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_text, (self.quit_button.x + 50, self.quit_button.y + 25))

import webbrowser
from pygame import mixer

class MusicScreen:
    def __init__(self, game):
        self.game = game
        self.font = pygame.font.Font(None, 50)
        mixer.init()  # Initialize the mixer for playing audio

        # Buttons setup for songs
        self.song_buttons = [
            pygame.Rect(game.screen_width // 2 - 100, 50 + i * 60, 200, 50) for i in range(6)
        ]
        self.songs = [
            "Audio/Songs/twinkle-twinkle.mp3",
            "Audio/Songs/happy-and-you-know-it.mp3",
            "Audio/Songs/idk.mp3",
            "Audio/Songs/my-year-zombies.mp3",
            "Audio/Songs/puff-the-magic-dragon.mp3",
            "Audio/Songs/body-bop-bop.mp3"
        ]
        self.song_labels = [f"Song {i+1}" for i in range(6)]

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
                    mixer.music.play()

            # Check if "Choose Your Own!" is clicked
            if self.choose_button.collidepoint(mouse_pos):
                webbrowser.open("https://www.youtube.com/")

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
        # Draw the song buttons
        for i, button in enumerate(self.song_buttons):
            pygame.draw.rect(screen, (0, 255, 0), button)
            song_text = self.font.render(self.song_labels[i], True, (255, 255, 255))
            screen.blit(song_text, (button.x + 50, button.y + 10))

        # Draw the "Choose Your Own!" button
        pygame.draw.rect(screen, (0, 255, 255), self.choose_button)
        choose_text = self.font.render("Choose Your Own!", True, (255, 255, 255))
        screen.blit(choose_text, (self.choose_button.x + 20, self.choose_button.y + 10))
        
        # Draw the "Back to the game!" button
        pygame.draw.rect(screen, (255, 255, 0), self.back_button)
        back_text = self.font.render("Back to the game!", True, (255, 255, 255))
        screen.blit(back_text, (self.back_button.x + 20, self.back_button.y + 10))

        # Draw the quit button
        pygame.draw.rect(screen, (255, 0, 0), self.quit_button)
        quit_text = self.font.render("Quit", True, (255, 255, 255))
        screen.blit(quit_text, (self.quit_button.x + 50, self.quit_button.y + 25))
