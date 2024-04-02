import RPi.GPIO as GPIO 


GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")



def button_callback(10):
    print("Button was pushed!")
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.FALLING,callback=button_callback) # Setup event on pin 10 rising edge
message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up