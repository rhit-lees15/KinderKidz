import tkinter as tk
import pygame
import sys
from pygame import mixer 
import led
import sound

def init():
# Initialize the game
    pygame.init()
    mixer.init()
    sound.play_intro()

    led.setup_and_run_leds()



    # mixer.music.load("Audio/whatsupcarmineletsdosomespelling.mp3")
    # mixer.music.set_volume(0.7)
    # mixer.music.play()
    
    # Set up the window size (width x height)
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("My Game")


    # Set up colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    red = (255, 0, 0)

    # Set up button fonts
    font = pygame.font.Font(None, 50)
    
    # Button texts
    start_text = font.render("Start", True, white)
    quit_text = font.render("Quit", True, white)
    
    # Button rectangles
    start_button = pygame.Rect(screen_width // 2 - 100, screen_height // 2 - 50, 200, 100)  # Centered button
    quit_button = pygame.Rect(screen_width // 2 - 100, screen_height - 120, 200, 80)  # Bottom button

    # Main loop
    running = True
    while running:
        screen.fill(black)  # Fill the screen with black
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            
            # Check for mouse click on buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if start_button.collidepoint(mouse_pos):
                    print("Game Started!")  # Replace with actual game logic
                if quit_button.collidepoint(mouse_pos):
                    running = False
        
        # Draw Start button
        pygame.draw.rect(screen, green, start_button)
        screen.blit(start_text, (start_button.x + 50, start_button.y + 25))
        
        # Draw Quit button
        pygame.draw.rect(screen, red, quit_button)
        screen.blit(quit_text, (quit_button.x + 50, quit_button.y + 25))


        # Update the display
        pygame.display.flip()
    
    pygame.quit()




    # root = tk.Tk()
    # root.title("My Game")
    # root.attributes('-fullscreen', True)
    # root.configure(bg = "black")


    #     # Add a label to the window (optional)
    # label = tk.Label(root, text="Welcome to the Game!", font=("Arial", 24))
    # label.pack(pady=20)
    
    # # Add a button to quit the game
    # quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 16))
    # quit_button.pack(pady=20)
    
    # # Start the Tkinter event loop
    # root.mainloop()
