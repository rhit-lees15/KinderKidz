import pygame

def playSound(filepath: str):
    pygame.mixer.init()
    my_sound = pygame.mixer.Sound(filepath)
    my_sound.play()
    pygame.time.wait(int(my_sound.get_length() * 1000))



if __name__ == "__main__":
    #playSound('sample.wav')
    playSound('sample2.mp3')




