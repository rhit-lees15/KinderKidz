import vlc
import time
import random

intro_sounds = ['./Media/Audio/hicarmineletsspellsomewordstoday.mp3','./Media/Audio/hicarmineareyoureadytospellsomewords.mp3','./Media/Audio/whatsupcarmineletsdosomespelling.mp3','./Media/Audio/letsspellsomewordstodaycarmine.mp3','./Media/Audio/hicarmineletsplaythespellinggame.mp3'] 
correct_letter_sounds = ['./Media/Audio/correctnowletsfindthenextletter.mp3','./Media/Audio/goodjobcarmineletsfindthenextletter.mp3','./Media/Audio/nicecarmineletsfindthenextletter.mp3','./Media/Audio/goodjobcarmine.mp3','./Media/Audio/greatjobcarmine.mp3'] 
next_word_sounds = ['./Media/Audio/greatjobnowletsspellthenextword.mp3','./Media/Audio/yayyouspelledthewordnowletsdothenextone.mp3','./Media/Audio/goodjobatspellingcarmineletsdothenextword.mp3','./Media/Audio/goodjobcarmine.mp3','./Media/Audio/greatjobcarmine.mp3'] 
wrong_order_sounds = ['./Media/Audio/soclosetrytofindadifferentletter.mp3','./Media/Audio/almostletstryadifferentorder.mp3','./Media/Audio/thatletterispartofthewordbutitsnottherightorder.mp3','./Media/Audio/soclosetryadifferentletter.mp3','./Media/Audio/oopsthatsnottherightlettertryadifferentone.mp3'] 
wrong_letter_sounds = ['./Media/Audio/almostthatletterisntpartoftheword.mp3','./Media/Audio/oopsthatletterisntpartofthewordtryadifferentone.mp3','./Media/Audio/soclosetryadifferentletter.mp3','./Media/Audio/oopsthatsnottherightlettertryadifferentone.mp3'] 
happy_sounds = ['./Media/Audio/90s-game-ui.mp3','./Media/Audio/copper-bell-ding-4.mp3','./Media/Audio/correct-choice.mp3','./Media/Audio/cute-level-up-1.mp3','./Media/Audio/cute-level-up-2.mp3','./Media/Audio/cute-level-up-3.mp3','./Media/Audio/game-bonus.mp3','./Media/Audio/level-up.mp3','./Media/Audio/level-up-2.mp3','./Media/Audio/YayKidsCrowd.mp3','./Media/Audio/bonus-points.mp3']
dance_break_sounds = ['./Media/Audio/hicarmineletstakeabreakchoosethesongyouwannadanceto.mp3','./Media/Audio/goodjobatspellingcarmineletstakeabreakanddance.mp3','./Media/Audio/okaycarminetimeforabreakletsdance.mp3'] 
choose_list_sounds = ['./Media/Audio/choosethelistofwordsthatyouwouldliketospell.mp3','./Media/Audio/itstimetochoosealistofwordstospell.mp3']


def init_vlc(sound_file:str):
        p = vlc.MediaPlayer(sound_file)
        p.play()
        time.sleep(1) #this is necessary because is_playing() returns false if called right away
        while p.is_playing():
            time.sleep(1)
        p.release()

def play_happy():
        init_vlc(random.choice(happy_sounds))

def play_intro():
        init_vlc(random.choice(intro_sounds))

def play_correct_letter():
        init_vlc(random.choice(correct_letter_sounds))

def play_next_word():
        init_vlc(random.choice(next_word_sounds))    

def play_wrong_order():
        init_vlc(random.choice(wrong_order_sounds))

def play_wrong_letter():
        init_vlc(random.choice(wrong_letter_sounds))

def play_dance_break():
        init_vlc(random.choice(dance_break_sounds))

def play_choose_list():
        init_vlc(random.choice(choose_list_sounds))
