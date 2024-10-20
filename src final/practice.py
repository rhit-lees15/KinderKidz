import pygame
import os
import random

# Initialize Pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_COLOR = WHITE

# Set the width and height of the screen (fullscreen can be set here)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Interactive GUI")

# Fonts
default_font = pygame.font.SysFont('Helvetica', 40)
small_font = pygame.font.SysFont('Helvetica', 20)

# Load images
# base_dir = os.path.dirname(os.path.abspath(__file__))
# rabbit_img = pygame.image.load(os.path.join(base_dir, "OLDCODE", "Images", "RABBIT.PNG"))
# cow_img = pygame.image.load(os.path.join(base_dir, "OLDCODE", "Images", "COW.PNG"))
# rabbit_img = pygame.transform.scale(rabbit_img, (200, 200))
# cow_img = pygame.transform.scale(cow_img, (200, 200))

# A function to display text on the screen
def display_text(text, font, color, center_x, center_y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(center_x, center_y))
    screen.blit(text_surface, text_rect)

# A function to create buttons and detect clicks
def button(text, color, rect, font, action=None):
    pygame.draw.rect(screen, color, rect)
    display_text(text, font, FONT_COLOR, rect[0] + rect[2] // 2, rect[1] + rect[3] // 2)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect[0] < mouse[0] < rect[0] + rect[2] and rect[1] < mouse[1] < rect[1] + rect[3]:
        if click[0] == 1 and action is not None:
            action()

# Define pages
def start_page():
    screen.fill(BLACK)
    screen.blit(rabbit_img, (SCREEN_WIDTH * 0.1, SCREEN_HEIGHT * 0.3))
    screen.blit(cow_img, (SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.3))

    display_text("Interactive GUI", default_font, FONT_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

    # Start and Exit buttons
    button("Start", GREEN, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, 200, 50), default_font, create_time_selection_page)
    button("Exit", RED, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 50), small_font, exit_program)

def time_selection_page():
    screen.fill(BLACK)
    display_text("Select Time", default_font, FONT_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)

    # Time buttons
    button("2 Minutes", BLUE, (SCREEN_WIDTH * 0.2 - 100, SCREEN_HEIGHT / 2, 200, 50), default_font, lambda: create_word_display_page(120))
    button("3.5 Minutes", BLUE, (SCREEN_WIDTH * 0.5 - 100, SCREEN_HEIGHT / 2, 200, 50), default_font, lambda: create_word_display_page(210))
    button("5 Minutes", BLUE, (SCREEN_WIDTH * 0.8 - 100, SCREEN_HEIGHT / 2, 200, 50), default_font, lambda: create_word_display_page(300))

    button("Exit", RED, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 50), small_font, exit_program)

def create_word_display_page(duration):
    screen.fill(BLACK)

    word_list = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
    random_word = random.choice(word_list)
    display_text(random_word, default_font, FONT_COLOR, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Start countdown
    create_countdown(duration)

def create_countdown(duration):
    start_ticks = pygame.time.get_ticks()

    while duration > 0:
        screen.fill(BLACK)

        # Calculate remaining time
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        remaining_time = duration - seconds

        if remaining_time <= 0:
            break

        # Display countdown
        display_text(f"Time Left: {remaining_time // 60}:{remaining_time % 60:02d}", small_font, FONT_COLOR, SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.1)

        # Exit button
        button("Exit", RED, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 100, 200, 50), small_font, exit_program)

        pygame.display.update()

def exit_program():
    pygame.quit()
    quit()

# Main loop
def main_loop():
    clock = pygame.time.Clock()

    current_page = start_page

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_program()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                exit_program()

        current_page()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main_loop()
