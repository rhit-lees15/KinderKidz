from audioplayer import AudioPlayer
import os
import RPi.GPIO as GPIO 
import vlc

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.




# import threading
# started = True

# def play_sound(pin):
#     print(pin)
#     sound_file = "sample2.mp3"
#     print("playing song" + sound_file)
#     sound = AudioPlayer("sample2.mp3").play()

# def play_sound2(pin):
#     print(pin)
#     sound_file = "sample.wav"
#     print("playing song" + sound_file)
#     sound = AudioPlayer("sample.wav").play()

# # Path to the sound file


# # Create a thread to play the sound
# sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
# sound_thread.start()

# # Continue with other tasks while the sound is playing

# while(started):
#     print("main thread")


from subprocess import *
import threading

# def play_sound(sound_file):
#     print("Playing sound:", sound_file)
#     subprocess.Popen(["afplay", sound_file])  # Use appropriate command based on your OS

# # Path to the sound file
# sound_file = "sample2.mp3"

# # Create a thread to play the sound
# sound_thread = threading.Thread(target=play_sound, args=(sound_file,))
# sound_thread.start()

# Continue with other tasks while the sound is playing

from subprocess import Popen, PIPE
import time


def handle_results(arg):
    print(arg)

    
# def play_my_sound(pinnumber):
#     print(pinnumber)
    
#     running_procs = [
#         Popen('cvlc sample2.mp3',shell=True, stdout=PIPE, stderr=PIPE)
#         ]
#     while running_procs:
#         for proc in running_procs:
            
#             stdout, stderr = proc.communicate()
#             print(stdout+stderr)
#             retcode = proc.poll()
#             if retcode is not None: # Process finished.
#                 running_procs.remove(proc)

#     inpu
                
# def play_my_sound2(pinnumber):
#     print(pinnumber)
#     running_procs = [
        
#         Popen('cvlc sample.wav',shell=True, stdout=PIPE, stderr=PIPE)
#         ]
#     while running_procs:
#         for proc in running_procs:
            
#             stdout, stderr = proc.communicate()
#             print(stdout+stderr)
#             retcode = proc.poll()
#             if retcode is not None: # Process finished.
#                 running_procs.remove(proc)
#                 break
#             else: # No process is done, wait a bit and check again.
#                 time.sleep(.1)
#                 continue

#         # Here, `proc` has finished with return code `retcode`
#         if retcode != 0:
#             """Error handling."""
#             print("bad")
#         handle_results(proc.stdout)




# def button_callback():
#     print("Button was pushed!")


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.add_event_detect(10,GPIO.FALLING,callback=play_sound) # Setup event on pin 10 rising edge
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
#GPIO.add_event_detect(24,GPIO.FALLING,callback=play_sound2) # Setup event on pin 10 rising edge
#message = input("Press enter to quit\n\n") # Run until someone presses enter


def init_vlc(song:str):
    vlc_instance = vlc.Instance()
    player = vlc_instance.media_player_new()

    media  = vlc_instance.media_new(song)
    media.get_mrl()
    player.set_media(media)
    player.play()
    # playing = set(State.playing)
    time.sleep(1.5) # startup time.
    duration = player.get_length() / 1000
    mm, ss   = divmod(duration, 60)

    # print("Current song is : ", song, "Length:", "%02d:%02d" % (mm,ss))

    time_left = True

    # the while loop checks every x seconds if the song is finished.
    # while time_left == True:
    #     song_time = player.get_state()
    #     print('song time to go: %s' % song_time)
    #     if song_time != vlc.State.Playing:
    #         print(song_time)
    #         time_left = False
    #     time.sleep(1) # if 1, then delay is 1 second.
    # print ('Finished playing your song')

while True:
    print("Reading Buttons!!")
    input_state = GPIO.input(10)
    if input_state == False:
        init_vlc('./sample.wav')
    input_state = GPIO.input(24)
    if input_state == False:
        init_vlc('./AudioStuff/sample2.mp3')
    time.sleep(1)


GPIO.cleanup() # Clean up


    
        
