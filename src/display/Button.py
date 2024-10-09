# Display LEDS, and respond when pushed
# from config import letters
from Media.GameSound import Audio
import random
# Raspberry Pi pin inputs that are used for each individual tile. 

# BUTTON_PINS = [17, 27, 22, 23, 24, 25, 16, 26]
# Current ground pin for the buttons is at pin 20

class Button:
        
    A = [13, 14, 15, 16, 23, 26, 32, 33, 36, 37, 42, 47, 51, 52, 53, 54, 55, 56, 57, 58, 61, 62, 67, 68, 71, 78, 81, 88]
    B = [13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 57, 52, 62,  67, 72, 77, 82, 83, 84, 85, 86]
    C = [13, 14, 15, 16, 22, 27, 38, 41, 58, 61, 72, 77, 83, 84, 85, 86]
    D = [14, 15, 16, 17, 22, 26, 32, 37, 42, 47, 52, 57, 62, 67, 73, 77, 82, 83, 84, 84, 85]
    E = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 57, 62, 77, 82, 83, 84, 85, 86, 87]
    F = [12, 13, 14, 15, 16, 17, 22, 37, 42, 43, 44, 45, 46, 47, 57, 62, 77, 82]
    G = [13, 14, 15, 16, 17, 21, 27, 38, 41, 53, 54, 58, 61, 67, 72, 78, 81, 87, 93, 94, 95, 96, 97]
    H = [12, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 52, 57, 62, 67, 72, 77, 82, 87]
    I = [12, 13, 14, 15, 16, 17, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 82, 83, 84, 85, 86, 87]
    J = [11, 12, 13, 14, 15, 16, 17, 25, 34, 45, 54, 62, 65, 74, 77, 82, 83, 84, 85]
    K = [12, 13, 17, 22, 25, 26, 34, 35, 37, 42, 43, 56, 57, 62, 64, 65, 73, 74, 77, 82, 86, 87]
    L = [18, 21, 38, 41, 58, 61, 78, 81, 82, 83, 84, 85, 86, 87]
    M = [11, 12, 13, 16, 17, 18, 21, 22, 23, 26, 27, 28, 31, 33, 36, 38, 41, 43, 44, 45, 46, 48, 51, 54, 55, 58, 61, 68, 71, 78, 81, 88]
    N = [11, 17, 18, 21, 22, 23, 28, 31, 36, 38, 41, 44, 48, 51, 54, 58, 61, 65, 66, 68, 71, 73, 78, 81, 87, 88]
    O = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 68, 72, 77, 83, 84, 85, 86]
    P = [12, 13, 14, 15, 16, 17, 22, 28, 31, 37, 42, 48, 52, 53, 54, 55, 56, 57, 62, 77, 82]
    Q = [13, 14, 15, 16, 22, 27, 31, 38, 41, 48, 51, 58, 61, 66, 68, 72, 77, 83, 84, 85, 86, 88]
    R = [12, 13, 14, 15, 16, 17, 22, 27, 32, 37, 42, 43, 44, 45, 46, 47, 55, 57, 62, 65, 73, 77, 82, 87]
    S = [12, 13, 14, 15, 16, 17, 118, 21, 38, 41, 52, 53, 54, 55, 56, 57, 68, 71, 82, 83, 84, 85, 86, 87]
    T = [11, 12, 13, 14, 15, 16, 17, 18, 24, 25, 34, 35, 44, 45, 54, 55, 64, 65, 74, 75, 84, 85]
    U = [11, 18, 21, 28, 31, 38, 41, 48, 51, 58, 61, 68, 71, 78, 82, 83, 84, 85, 86, 87]
    V = [11, 18, 21, 28, 31, 38, 42, 47, 52, 57, 63, 66, 73, 76, 84, 85]
    W = [11, 18, 21, 28, 31, 38, 41, 44, 45, 48, 51, 54, 55, 58, 61, 63, 66, 68, 71, 73, 76, 78, 82, 87]
    X = [11, 18, 22, 27, 33, 36, 44, 45, 54, 55, 63, 66, 72, 77, 81, 88]
    Y = [11, 18, 21, 22, 27, 28, 32, 33, 36, 37, 43, 46, 54, 55, 64, 65, 74, 75, 84, 85]
    Z = [11, 12, 13, 14, 15, 16, 17, 18, 28, 32, 33, 45, 55, 62, 63, 78, 81, 82, 83, 84, 85, 86, 87, 88]


    letters = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J,
        'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T,
        'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z}
        

    # Function to generate additional random letters
    def generateRandomLetters(remainingLetters, numLetters):
        return random.sample(remainingLetters, numLetters)
    # Function to add all letters to one string and shuffle them
    def randomizeLetters(word, letters):
        allLetters = list(word + ''.join(letters))
        random.shuffle(allLetters)
        return ''.join(allLetters)
    
    def newWord():
        global spelledWord, randomWord, randomizedLetters, button_sequence, button_letters
        
    ## NOOR NEW ADDITION 05.09.24
        word_list.remove(randomWord)
        
        if not word_list:
            print("Congratulations! You've spelled all the words in the list!")
            return
        
        
        ################# END OF ADDITION
        # Generate a new word
        n = 0
        while n <= len(word_list) - 1:
            randomWord = word_list[n]
            n += 1
        
        # Get remaining letters
        availableLetters = list(set(string.ascii_uppercase) - set(spelledWord) - set(randomWord))
        # availableLetters = list(set(string.ascii_uppercase) - set(randomWord))
        # Generate additional random letters
        randomLetters = generateRandomLetters(availableLetters, 8 - len(randomWord))
        
        # Combine the random word and random letters into a single string and shuffle them
        randomizedLetters = randomizeLetters(randomWord, randomLetters)
        
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

        
