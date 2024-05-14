import vlc
import time
import random


def init_vlc(sound_file:str):
    p = vlc.MediaPlayer(sound_file)
    p.play()
    time.sleep(0.2) #this is necessary because is_playing() returns false if called right away
    while p.is_playing():
        time.sleep(0.02)
    p.release()

intro_sounds = ['./AudioStuff/hicarmineletsspellsomewordstoday.mp3','./AudioStuff/hicarmineareyoureadytospellsomewords.mp3','./AudioStuff/whatsupcarmineletsdosomespelling.mp3','./AudioStuff/letsspellsomewordstodaycarmine.mp3','./AudioStuff/hicarmineletsplaythespellinggame.mp3'] 
correct_letter_sounds = ['./AudioStuff/correctnowletsfindthenextletter.mp3','./AudioStuff/goodjobcarmineletsfindthenextletter.mp3','./AudioStuff/nicecarmineletsfindthenextletter.mp3','./AudioStuff/goodjobcarmine.mp3','./AudioStuff/greatjobcarmine.mp3'] 
next_word_sounds = ['./AudioStuff/greatjobnowletsspellthenextword.mp3','./AudioStuff/yayyouspelledthewordnowletsdothenextone.mp3','./AudioStuff/goodjobatspellingcarmineletsdothenextword.mp3','./AudioStuff/goodjobcarmine.mp3','./AudioStuff/greatjobcarmine.mp3'] 
wrong_order_sounds = ['./AudioStuff/soclosetrytofindadifferentletter.mp3','./AudioStuff/almostletstryadifferentorder.mp3','./AudioStuff/thatletterispartofthewordbutitsnottherightorder.mp3','./AudioStuff/soclosetryadifferentletter.mp3','./AudioStuff/oopsthatsnottherightlettertryadifferentone.mp3'] 
wrong_letter_sounds = ['./AudioStuff/almostthatletterisntpartoftheword.mp3','./AudioStuff/oopsthatletterisntpartofthewordtryadifferentone.mp3','./AudioStuff/soclosetryadifferentletter.mp3','./AudioStuff/oopsthatsnottherightlettertryadifferentone.mp3'] 
happy_sounds = ['./AudioStuff/90s-game-ui.mp3','./AudioStuff/copper-bell-ding-4.mp3','./AudioStuff/correct-choice.mp3','./AudioStuff/cute-level-up-1.mp3','./AudioStuff/cute-level-up-2.mp3','./AudioStuff/cute-level-up-3.mp3','./AudioStuff/game-bonus.mp3','./AudioStuff/level-up.mp3','./AudioStuff/level-up-2.mp3','./AudioStuff/YayKidsCrowd.mp3','./AudioStuff/bonus-points.mp3']
dance_break_sounds = ['./AudioStuff/hicarmineletstakeabreakchoosethesongyouwannadanceto.mp3','./AudioStuff/goodjobatspellingcarmineletstakeabreakanddance.mp3','./AudioStuff/okaycarminetimeforabreakletsdance.mp3'] 

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


# # intro sounds
# ./AudioStuff/hicarmineletsspellsomewordstoday.mp3
# ./AudioStuff/hicarmineareyoureadytospellsomewords.mp3
# ./AudioStuff/whatsupcarmineletsdosomespelling.mp3
# ./AudioStuff/letsspellsomewordstodaycarmine.mp3
# ./AudioStuff/hicarmineletsplaythespellinggame.mp3

# # correct letter sounds
# ./AudioStuff/correctnowletsfindthenextletter.mp3
# ./AudioStuff/goodjobcarmineletsfindthenextletter.mp3
# ./AudioStuff/nicecarmineletsfindthenextletter.mp3
# ./AudioStuff/goodjobcarmine.mp3
# ./AudioStuff/greatjobcarmine.mp3

# # next word sounds
# ./AudioStuff/greatjobnowletsspellthenextword.mp3
# ./AudioStuff/yayyouspelledthewordnowletsdothenextone.mp3
# ./AudioStuff/goodjobatspellingcarmineletsdothenextword.mp3
# ./AudioStuff/goodjobcarmine.mp3
# ./AudioStuff/greatjobcarmine.mp3


# # happy sounds
# ./AudioStuff/90s-game-ui.mp3
# ./AudioStuff/copper-bell-ding-4.mp3
# ./AudioStuff/correct-choice.mp3
# ./AudioStuff/cute-level-up-1.mp3
# ./AudioStuff/cute-level-up-2.mp3
# ./AudioStuff/cute-level-up-3.mp3
# ./AudioStuff/game-bonus.mp3
# ./AudioStuff/level-up.mp3
# ./AudioStuff/level-up-2.mp3
# ./AudioStuff/YayKidsCrowd.mp3
# ./AudioStuff/bonus-points.mp3

# # wrong order sounds
# ./AudioStuff/soclosetrytofindadifferentletter.mp3
# ./AudioStuff/almostletstryadifferentorder.mp3
# ./AudioStuff/thatletterispartofthewordbutitsnottherightorder.mp3
# ./AudioStuff/soclosetryadifferentletter.mp3
# ./AudioStuff/oopsthatsnottherightlettertryadifferentone.mp3

# # wrong letter sounds
# ./AudioStuff/almostthatletterisntpartoftheword.mp3
# ./AudioStuff/oopsthatletterisntpartofthewordtryadifferentone.mp3
# ./AudioStuff/soclosetryadifferentletter.mp3
# ./AudioStuff/oopsthatsnottherightlettertryadifferentone.mp3

# # dance break sounds
# ./AudioStuff/hicarmineletstakeabreakchoosethesongyouwannadanceto.mp3
# ./AudioStuff/goodjobatspellingcarmineletstakeabreakanddance.mp3
# ./AudioStuff/okaycarminetimeforabreakletsdance.mp3
