import pygame
import sys
import led
from pathlib import Path
from pygame import mixer
from screens import MainScreen
from screens import TimerScreen
from screens import MusicScreen

class Game:
    def __init__(self):
        pygame.init()
        mixer.init()

        # Load background music
        mixer.music.load(open(Path(__file__).parent.parent / "Audio" / "whatsupcarmineletsdosomespelling.mp3", 'r'))
        
        mixer.music.set_volume(0.7)
        mixer.music.play()

        # Set up the window
        self.screen_width, self.screen_height = 800, 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("My Game")

        # Initialize screen state
        self.current_screen = MainScreen(self)

    def switch_screen(self, new_screen):
        """Switch to a new screen."""
        self.current_screen = new_screen(self)

    def run(self):
        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Fill screen with black
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                # Let the current screen handle its events
                self.current_screen.handle_event(event)

            # Update and draw the current screen
            self.current_screen.update()
            self.current_screen.draw(self.screen)

            pygame.display.flip()  # Update the display

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
