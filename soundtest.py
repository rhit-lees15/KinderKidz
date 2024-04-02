from audioplayer import AudioPlayer
import os
import RPi.GPIO as GPIO 

# Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.




# import threading
# started = True

# def play_sound(sound_file):
#     print("playing song" + sound_file)
#     sound = AudioPlayer("sample2.mp3").play()

# # Path to the sound file
# sound_file = "sample2.mp3"

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

running_procs = [
    Popen('cvlc sample2.mp3',shell=True, stdout=PIPE, stderr=PIPE)
    ]




while running_procs:
    
    for proc in running_procs:

        stdout, stderr = proc.communicate()
        print(stdout+stderr)
        retcode = proc.poll()
        if retcode is not None: # Process finished.
            running_procs.remove(proc)
            break
        else: # No process is done, wait a bit and check again.
            time.sleep(.1)
            continue

    # Here, `proc` has finished with return code `retcode`
    if retcode != 0:
        """Error handling."""
        print("bad")
    #handle_results(proc.stdout)

def handle_reults(arg):
    print(arg)


def button_callback(10):
    print("Button was pushed!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up

    
        