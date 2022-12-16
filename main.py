import tkinter as tk 
import time
import random


# ------------------------------- VARIABLES ---------------------------------- # 
count = 60
errors = 0
wpm = 0
error_list = []

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
    global errors
    global wpm
    global error_list

    og_text = []
    submitted_text = []

    submission = input.get("1.0", 'end')
    
    for letter in text:
        og_text.append(letter)

    for letter in submission:
        submitted_text.append(letter)

    error_list = [item for item in submitted_text if item not in og_text]
    errors = len(error_list)

    total_wpm = len(submission.split())
    wpm = total_wpm - errors

    score.config(text=f"Your score is {wpm} words per minute")

# ------------------------- TEST MATERIAL ----------------------- # 
possibleText = [
    "An ever-growing number of complex and rigid rules plus hard-to-cope-with regulations are now being legislated from state to state. Key federal regulations were formulated by the FDA, FTC, and the CPSC. Each of these federal agencies serves a specific mission. One example: Laws sponsored by the Office of the Fair Debt Collection Practices prevent an agency from purposefully harassing clients in serious debt. The Fair Packaging and Labeling Act makes certain that protection from misleading packaging of goods is guaranteed to each buyer of goods carried in small shops as well as in large supermarkets. Products on the market must reveal the names of all ingredients on the label. Language must be in clear and precise terms that can be understood by everyone. This practice is very crucial for the lives of many people. It is prudent that we recall that the FDA specifically requires that all goods are pure, safe, and wholesome. The FDA states that all goods be produced under highly sanitary conditions. Drugs must be completely safe and must also be effective for their stated purpose. This policy applies to cosmetics that must be both safe and pure. Individuals are often totally unappreciative of the FDA's great dedication.",

    "The first personnel management department started at the National Cash Register Co. in 1900. The owner, John Henry Patterson, organized a personnel department to deal with grievances, discharges and safety, and training for supervisors on new laws and practices after several strikes and employee lockouts. During the 1970s, companies experienced globalization, deregulation, and rapid technological change which caused the major companies to enhance their strategic planning and focus on ways to promote organizational effectiveness. This resulted in developing more jobs and opportunities for people to show their skills which were directed to effective applying employees toward the fulfillment of individual, group, and organizational goals. Many years later the major/minor of human resource management was created at universities and colleges also known as business administration.",

    "A transcription service is a business which converts speech (either live or recorded) into a written or electronic text document. Transcription services are often provided for business, legal, or medical purposes. The most common type of transcription is from a spoken-language source into text such as a computer file suitable for printing as a document such as a report. Common examples are the proceedings of a court hearing such as a criminal trial (by a court reporter) or a physician's recorded voice notes (medical transcription)."
]


text = random.choice(possibleText)

# ---------------------------- UI Setup -------------------------- #
window = tk.Tk()
window.title('Typing Speed Test')
window.geometry('700x700')


# start Button
count_down_button = tk.Button(master=window, text="Start", padx=10, pady=10, command=countdown)
count_down_button.grid(row=0, column=0)

# restart Button
button = tk.Button(master=window, text="Restart",  padx=10, pady=10, command=countdown)
button.grid(row=0, column=1)


totype = tk.Label(window, text=text, wraplength=600)
totype.grid(row=1, column=0, columnspan=3)

input = tk.Text(window)
input.grid(row=2, column=0, columnspan=3)

timer = tk.Label(text="00:60")
timer.grid(row=3, column=0)

score = tk.Label(text="Your score is: ")
score.grid(row=3, column=1, columnspan=2)

window.mainloop()
