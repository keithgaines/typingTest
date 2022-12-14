import tkinter as tk 
import time
import random


# ------------------------------- VARIABLES ---------------------------------- # 
count = 60
errors = 0
wpm = 0

# ------------------------------ TIMER MERCHANISM --------------------------- # 

def countdown():
    global count
    if count > 0:
        window.after(1000, countdown)
        count  -= 1
        timer.config(text=count)
    if count == 0:
        checkerrors()

# ------------------------------ FUNCTIONS -------------------------------- # 

def checkerrors():
    global text
    global error
    global wpm

    og_text = []
    submitted_text = []

    submission = input.get()
    
    for letter in text:
        og_text.append(letter)

    for letter in submission:
        submitted_text.append(letter)

    for letter in submitted_text:
        if submitted_text(letter) == og_text(letter):
            pass
        else:
            error += 1
    
    wpm = len(submission.split())
    score.config(text=f"Your score is {wpm} words per minute")



# ------------------------- TEST MATERIAL ----------------------- # 
possibleText = [
    "I'm here today to introduce the next phase. The next step in the big Bart craze. I've got a dance real easy to do; I learned it with no rhythm, and so can you. So move your body if you've got the notion, Front to back in a rock-like motion. Now that you've got it, if you think you can, do it to the music. That's the Bartman."
]
text = random.choice(possibleText).lower()



# ---------------------------- UI Setup -------------------------- #
window = tk.Tk()
window.title('Typing Speed Test')
window.geometry('1000x1000')


# start Button
count_down_button = tk.Button(master=window, text="Start", padx=30, pady=30, command=countdown)
count_down_button.grid(row=0, column=0)

# restart Button
# button = tk.Button(master=window, text="Restart", command=count_time)
# button.place(relx=0.7, rely=0.2,anchor=tk.CENTER)


totype = tk.Label(window, width=60, height=10, text=text, wraplength=900)
totype.grid(row=1, column=0, columnspan=3)

input = tk.Text(window, width=60, height=10, padx=20, pady=20)
input.grid(row=2, column=0, columnspan=3)

timer = tk.Label(text="00:60")
timer.grid(row=3, column=0)

score = tk.Label(text="Your score is: ")
score.grid(row=3, column=1, columnspan=2)

window.mainloop()