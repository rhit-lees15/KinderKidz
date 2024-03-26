# import the time module 
import time 
  
# define the countdown func. 
def countdown(t): 
   
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        t -= 1
      
    print('Dance Time!') 
  
import vlc

song = vlc.MediaPlayer('song.mp3')
song.play()
song.set_time(10000)    # play at 10,000 ms (10 seconds)

# input time in seconds 
t = input("Enter the time in seconds: ") 
  
# function call 
countdown(int(t))