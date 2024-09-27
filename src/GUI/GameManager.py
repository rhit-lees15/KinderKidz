# game_sound needs to be removed and replaced with new location, or create a new function in 
# specified file to play when necessary


import random
import time

class Game:
    # Dictionary of all the words included in the spelling game
    self.word_lists = {
        "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
        "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
        "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
        }
    
    # Time of duration
    duration = 30

    # Countdown timer that is displayed at the top right of the GUI to indicate the amount of time Carmine has to complete the lesson
    def create_countdown(self, frame, duration):
        countdown_label = tk.Label(frame, font=("Helvetica", 16))
        countdown_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

    def update_countdown(duration):    
            
        min, sec = divmod(duration,60)
        countdown_label.config(text=f"Time Left: {min}:{sec}", bg = "black", fg = "white")


        if duration > 0:
            frame.after(1000, update_countdown, duration - 1)
        else:
            self.create_dance_display_page()

    update_countdown(duration)
    
    # Function to create a list of additional letters to include, dependent on the length of the word
    def gen_random_letters(remainingLetters, numLetters):
        return random.sample(remainingLetters, numLetters)
    
    # Function to add all letters to one string and shuffle them
    def randomize_Letters(word, letters):
        allLetters = list(word + ''.join(letters))
        random.shuffle(allLetters)
        return ''.join(allLetters)
    

    # Generate a new random word from the selected word list
    random_word = random.choice(self.word_lists[word_list_name])

    letter = button_letters[pin]
    # time.sleep(0.25)
    if letter in randomWord:
        # Check if the letter is in the correct position
        if letter == randomWord[len(spelledWord)]:
            ## The letter is in the word
            spelledWord += letter
            # print("Current spelling:", spelledWord)
            if len(spelledWord) != len(randomWord):
                ## The letter is in correct position - correct
                #correct_light(pin)
                correct_light(letter, pin)
                gamesound.play_happy()
                gamesound.play_correct_letter()
            # If the full word is spelled correctly
            elif len(spelledWord) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                correct_light(letter, pin)
                gamesound.play_happy()
                turn_off()
                gamesound.play_next_word()
                newWord()
                initialize_letter(randomizedLetters)

        else:
            # Find the first incorrect letter position

            #incorrect_position = spelledWord[]
            # restart_from = randomWord.index(spelledWord[incorrect_position])
            if len(spelledWord) == 0:
                # print("Incorrect order!")
                #spelledWord = ''
                gamesound.play_wrong_order()
                # print("Current spelling:", spelledWord)
            else:
                #spelledWord = randomWord[incorrect_position]
                # print("Incorrect order! Restarting from:", spelledWord)
                gamesound.play_wrong_order()
    else:
        # print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        wrong_light(letter, pin)
        gamesound.play_wrong_letter()
        
    def newWord():
    global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
    
## NOOR NEW ADDITION 05.09.24
    wordList.remove(randomWord)
    
    if not wordList:
        print("Congratulations! You've spelled all the words in the list!")
        return
    
    # Generate a new word
    n = 0
    while n <= len(wordList) - 1:
        randomWord = wordList[n]
        n += 1
    
    # Get remaining letters
    availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
    # availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
    # Generate additional random letters
    randomLetters = gen_random_letters(availableLetters, 8 - len(randomWord))
    
    # Combine the random word and random letters into a single string and shuffle them
    randomizedLetters = randomize_letters(randomWord, randomLetters)
    
    # Map each letter to a button
    button_letters = {}
    for idx, pin in enumerate(BUTTON_PINS):
        button_letters[pin] = randomizedLetters[idx]
    
    # Set button sequence for the new word
    button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]
    
    # Print new word and letters
    # init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    # print("Reallocated letters: " + ' '.join(randomizedLetters))
    # print("Available letters: " + ' '.join(availableLetters))
    
    # Reset spelledWord
    spelledWord = ''
