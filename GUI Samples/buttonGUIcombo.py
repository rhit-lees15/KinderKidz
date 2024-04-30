import tkinter as tk
import random
import string
import time
import vlc

# Function to generate a random word
def generateRandomWord(words):
    return random.choice(words)

# Function to generate additional random letters
def generateRandomLetters(remainingLetters, numLetters):
    return random.sample(remainingLetters, numLetters)

# Function to add all letters to one string and shuffle them
def randomizeLetters(word, letters):
    allLetters = list(word + ''.join(letters))
    random.shuffle(allLetters)
    return ''.join(allLetters)

# Function to initialize VLC and play audio
def init_vlc(sound_file:str):
    p = vlc.MediaPlayer(sound_file)
    p.play()
    time.sleep(1) #this is necessary because is_playing() returns false if called right away
    while p.is_playing():
        time.sleep(1)
    p.release()

# Function to handle button press event
def buttonPress(pin):
    global spelledWord, randomWord
    
    letter = button_letters[pin]
    if letter in randomWord:
        if letter == randomWord[len(spelledWord)]:
            spelledWord += letter
            print("Current spelling:", spelledWord)
            if len(spelledWord) != len(randomWord):
                init_vlc('./AudioStuff/goodjobnowletsfindthenextletter.mp3')
            elif len(spelledWord) == len(randomWord):
                print("Correct! You spelled the word correctly.")
                init_vlc('./AudioStuff/timetomoveontothenextword.mp3')
                newWord()
        else:
            if len(spelledWord) == 0:
                print("Incorrect order!")
                init_vlc('./AudioStuff/oopsthatsnotrighttryadifferentorder.mp3')
                print("Current spelling:", spelledWord)
            else:
                print("Incorrect order! Restarting from:", spelledWord)
                init_vlc('./AudioStuff/oopsthatsnotrighttryadifferentorder.mp3')
    else:
        print(f"Incorrect! Button {pin} ({letter}) is not part of the word. Try again.")
        init_vlc('./AudioStuff/nopethatletterisntpartoftheword.mp3')

# Function to generate and display a new word
def newWord():
    global spelledWord, randomWord, randomizedLetters, button_letters
    
    randomWord = generateRandomWord(wordList)
    availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
    randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))
    randomizedLetters = randomizeLetters(randomWord, randomLetters)
    
    button_letters = {}
    for idx, pin in enumerate(BUTTON_PINS):
        button_letters[pin] = randomizedLetters[idx]
    
    button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]
    
    print("Let's spell another word.")
    print(f"Spell the word: {randomWord}")
    print("Reallocated letters: " + ' '.join(randomizedLetters))
    
    spelledWord = ''

# Initialize Tkinter
root = tk.Tk()
root.configure(background='black')
root.geometry("800x600")

# Start Page
start_frame = tk.Frame(root, bg='black')
start_frame.pack(expand=True)

start_image = tk.PhotoImage(file="path/to/image.png")
start_label = tk.Label(start_frame, image=start_image, bg='black')
start_label.place(relx=0.5, rely=0.5, anchor='center')

start_button = tk.Button(start_frame, text="Start", bg='green', fg='white', font=('Helvetica', 16))
start_button.place(relx=0.5, rely=0.5, anchor='center')

exit_button = tk.Button(start_frame, text="Exit", bg='red', fg='white', font=('Helvetica', 16))
exit_button.pack(side=tk.BOTTOM, pady=20)

# Game Page
game_frame = tk.Frame(root, bg='black')
game_label = tk.Label(game_frame, text="", font=('Helvetica', 24), bg='black', fg='white')
game_label.pack()

# Function to switch to the game page
def start_game():
    start_frame.pack_forget()
    game_frame.pack(expand=True)
    newWord()

# Function to handle timer selection
def select_timer(timer):
    print("Timer selected:", timer)

# Bind button clicks
start_button.config(command=start_game)
exit_button.config(command=root.destroy)

# Timer selection buttons
timer_5_button = tk.Button(game_frame, text="5 sec", command=lambda: select_timer(5))
timer_5_button.pack()

timer_30_button = tk.Button(game_frame, text="30 sec", command=lambda: select_timer(30))
timer_30_button.pack()

timer_60_button = tk.Button(game_frame, text="1 min", command=lambda: select_timer(60))
timer_60_button.pack()

# GPIO Pins for buttons
BUTTON_PINS = [24, 25, 8, 7, 5, 6, 13, 12]

# Generate a random word
wordList = ['CAT', 'DOG', 'CAR', 'BAG', 'HAT', 'LEG', 'ONE', 'MAT']
randomWord = generateRandomWord(wordList)

# Get remaining letters
availableLetters = list(set(string.ascii_uppercase) - set(randomWord))

# Generate additional random letters
randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))

# Combine the random word and random letters into a single string and shuffle them
randomizedLetters = randomizeLetters(randomWord, randomLetters)

# Map each letter to a button
button_letters = {}
for idx, pin in enumerate(BUTTON_PINS):
    button_letters[pin] = randomizedLetters[idx]

# Set button sequence for the initial word
button_sequence = [BUTTON_PINS[randomizedLetters.index(letter)] for letter in randomWord]

root.mainloop()
