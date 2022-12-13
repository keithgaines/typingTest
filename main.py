import tkinter as tk 
import time
import random

possibleText = [
    "I'm here today to introduce the next phase. The next step in the big Bart craze. I've got a dance real easy to do; I learned it with no rhythm, and so can you. So move your body if you've got the notion, Front to back in a rock-like motion. Now that you've got it, if you think you can, do it to the music. That's the Bartman."
]
text = random.choice(possibleText).lower()


# calculate the accuracy of input prompt
def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(text)):
        if i in (0, len(text)-1):
            if text[i] == text[i]:
                continue
            else:
                errors +=1
        else:
            if iwords[i] == words[i]:
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

# calculate the speed in words per minute
def typingSpeed(iprompt, stime, etime):
    global time
    global text

    text = text.split()
    twords = len(text)
    speed = twords / time

    return speed

# calculate total time elapsed
def start_timer():
    timenow = time.time()
    timeend = timenow  + 2
    if timeend == time.time():
        countwords()

def countwords():
    score = typingSpeed - typingErrors
    return score




# UI Setup
window = tk.Tk()
window.title('Typing Speed Test')
window.geometry('1000x1000')


# start Button
count_down_button = tk.Button(master=window, text="Start", command=start_timer)
count_down_button.grid(row=0, column=0)

# restart Button
# button = tk.Button(master=window, text="Restart", command=count_time)
# button.place(relx=0.7, rely=0.2,anchor=tk.CENTER)

totype = tk.Text(window, width=60, height=10)
totype.grid(row=1, column=0, columnspan=3)
totype.insert(tk.END, text)

typed_text= tk.Text(window, width=60,height=10)
typed_text.grid(row=2, column=0, columnspan=3)

all_text_list = totype.get('1.0','end-1c').split()
typed_text_list = typed_text.get('1.0','end-1c').split()

score_lbl = tk.Label(master=window, text=f"Your Test Score: {countwords} per minute") 
score_lbl.grid(row=3, column=0)

window.mainloop()