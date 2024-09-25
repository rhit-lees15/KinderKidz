
if __name__ == '__main__':
    #####* Start the game
    # Initialization of lights    
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()
    # Create NeoPixel object with appropriate configuration.
    ### TODO: DisplayManager.py
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()
    # #-------------------------------------THREADING ATTEMPT
    # thread = Tread(target = threaded_function, args = (10, ))
    # thread.start()
    # tread.join()
    # print("Thread finished.....exiting")
    # #--------------------------------------------THREADING

    ### TODO: game.py
    print("Welcome to the Word Spelling Game!")
    gamesound.play_intro()
    print(f"Spell the word: {randomWord}")

    initialize_letter(randomizedLetters)
    try:
        while words_remaining:
            if not wordList:
                words_remaining = False
                
            time.sleep(0.25)
        else:
             turn_off()

            
    except KeyboardInterrupt:
        turn_off()
        GPIO.cleanup()