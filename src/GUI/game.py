import random
import time

# Countdown timer that is displayed at the top right of the GUI to indicate the amount of time Carmine has to complete the lesson
def create_countdown(self, frame, duration):
    countdown_label = tk.Label(frame, font=("Helvetica", 16))
    countdown_label.place(relx=0.8, rely=0.1, anchor=tk.CENTER)

# Time of duration
duration = 30

def update_countdown(duration):    
        
    min, sec = divmod(duration,60)
    countdown_label.config(text=f"Time Left: {min}:{sec}", bg = "black", fg = "white")


    if duration > 0:
        frame.after(1000, update_countdown, duration - 1)
    else:
        self.create_dance_display_page()

update_countdown(duration)

# Generate a new random word from the selected word list
   random_word = random.choice(self.word_lists[word_list_name])


self.word_lists = {
    "List 1": ['MY', 'THIS', 'A', 'IS', 'HOME'],
    "List 2": ['THE', 'IN', 'CITY', 'BY', 'OCEAN'],
    "List 3": ['ON', 'NOT', 'FARM', 'LIKE', 'I']
    }