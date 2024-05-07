import vlc
import time
import random


def init_vlc(sound_file:str):
    p = vlc.MediaPlayer(sound_file)
    p.play()
    time.sleep(1) #this is necessary because is_playing() returns false if called right away
    while p.is_playing():
        time.sleep(1)
    p.release()

intro_sounds = ['','',''] #insert different sounds
correct_letter_sounds = ['','',''] #insert different sounds
next_word_sounds = ['','',''] #insert different sounds
wrong_order_sounds = ['','',''] #insert different sounds
wrong_letter_sounds = ['','',''] #insert different sounds
happy_sounds = ['./AudioStuff/90s-game-ui.mp3','./AudioStuff/copper-bell-ding-4','/AudioStuff/correct-choice'] #insert different sounds
transition_sounds = ['','',''] #insert different sounds

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

def play_transition():
    init_vlc(random.choice(transition_sounds))


# intro sounds
# ./AudioStuff/hicarmineletsspellsomewordstoday
# ./AudioStuff/hicarmineareyoureadytospellsomewords
# ./AudioStuff/whatsupcarmineletsdosomespelling
# ./AudioStuff/letsspellsomewordstodaycarmine
# ./AudioStuff/hicarmineletsplaythespellinggame

# correct letter sounds
# ./AudioStuff/correctnowletsfindthenextletter
# ./AudioStuff/goodjobcarmineletsfindthenextletter
# ./AudioStuff/nicecarmineletsfindthenextletter
# ./AudioStuff/goodjobcarmine
# ./AudioStuff/greatjobcarmine

# next word sounds
./AudioStuff/greatjobnowletsspellthenextword
./AudioStuff/yayyouspelledthewordnowletsdothenextone
./AudioStuff/
./AudioStuff/
./AudioStuff/

# happy sounds
# ./AudioStuff/90s-game-ui.mp3
# ./AudioStuff/copper-bell-ding-4
# ./AudioStuff/correct-choice
# ./AudioStuff/cute-level-up-1
# ./AudioStuff/cute-level-up-2
# ./AudioStuff/cute-level-up-3
# ./AudioStuff/game-bonus
# ./AudioStuff/level-up
# ./AudioStuff/level-up-2
# ./AudioStuff/YayKidsCrowd
# ./AudioStuff/bonus-points


