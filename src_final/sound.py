import random
import string
import pygame
import os


# Paths for audio files
audio_folder = 'Audio/'
intro_sounds = [os.path.join(audio_folder, file) for file in ['hicarmineletsspellsomewordstoday.mp3','hicarmineareyoureadytospellsomewords.mp3','whatsupcarmineletsdosomespelling.mp3','letsspellsomewordstodaycarmine.mp3','hicarmineletsplaythespellinggame.mp3']]
correct_letter_sounds = [os.path.join(audio_folder, file) for file in ['correctnowletsfindthenextletter.mp3','goodjobcarmineletsfindthenextletter.mp3','nicecarmineletsfindthenextletter.mp3','goodjobcarmine.mp3','greatjobcarmine.mp3']]
next_word_sounds = [os.path.join(audio_folder, file) for file in ['greatjobnowletsspellthenextword.mp3','yayyouspelledthewordnowletsdothenextone.mp3','goodjobatspellingcarmineletsdothenextword.mp3','goodjobcarmine.mp3','greatjobcarmine.mp3']]
wrong_order_sounds = [os.path.join(audio_folder, file) for file in ['soclosetrytofindadifferentletter.mp3','almostletstryadifferentorder.mp3','thatletterispartofthewordbutitsnottherightorder.mp3','soclosetryadifferentletter.mp3','oopsthatsnottherightlettertryadifferentone.mp3']]
wrong_letter_sounds = [os.path.join(audio_folder, file) for file in ['almostthatletterisntpartoftheword.mp3','oopsthatletterisntpartofthewordtryadifferentone.mp3','soclosetryadifferentletter.mp3','oopsthatsnottherightlettertryadifferentone.mp3']]
happy_sounds = [os.path.join(audio_folder, file) for file in ['90s-game-ui.mp3','copper-bell-ding-4.mp3','correct-choice.mp3','cute-level-up-1.mp3','cute-level-up-2.mp3','cute-level-up-3.mp3','game-bonus.mp3','level-up.mp3','level-up-2.mp3','YayKidsCrowd.mp3','bonus-points.mp3']]
dance_break_sounds = [os.path.join(audio_folder, file) for file in ['hicarmineletstakeabreakchoosethesongyouwannadanceto.mp3','goodjobatspellingcarmineletstakeabreakanddance.mp3','okaycarminetimeforabreakletsdance.mp3']]
choose_list_sounds = [os.path.join(audio_folder, file) for file in ['choosethelistofwordsthatyouwouldliketospell.mp3','itstimetochoosealistofwordstospell.mp3']]

class Audio:
    @staticmethod
    def play_sound(sound_file: str):
        """Play a sound file."""
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play()

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)  # Check every 100 ms

    @staticmethod
    def play_happy():
        Audio.play_sound(random.choice(happy_sounds))

    @staticmethod
    def play_intro():
        Audio.play_sound(random.choice(intro_sounds))

    @staticmethod
    def play_correct_letter():
        Audio.play_sound(random.choice(correct_letter_sounds))

    @staticmethod
    def play_next_word():
        Audio.play_sound(random.choice(next_word_sounds))

    @staticmethod
    def play_wrong_order():
        Audio.play_sound(random.choice(wrong_order_sounds))

    @staticmethod
    def play_wrong_letter():
        Audio.play_sound(random.choice(wrong_letter_sounds))

    @staticmethod
    def play_dance_break():
        Audio.play_sound(random.choice(dance_break_sounds))

    @staticmethod
    def play_choose_list():
        Audio.play_sound(random.choice(choose_list_sounds))