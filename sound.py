import pygame
import wave
import math

def playSound(filepath: str):
    # pygame.mixer.init()
    # my_sound = pygame.mixer.Sound(filepath)
    # my_sound.play()
    # pygame.time.wait(int(my_sound.get_length() * 1000))

    frequence = math.ceil(wave.open(filepath).getframerate())
    print(frequence)
    pygame.mixer.init(frequency=frequence)
   
    
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




if __name__ == "__main__":
    playSound('sample.wav')




