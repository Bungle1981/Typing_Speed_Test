from tkinter import *
from timeit import default_timer as timer
import random

# Dictionary of sentences that can be selected
SENTENCES = {
    1:{"sentence": "The quick brown fox jumps over the lazy dog.", "length": 9},
    2:{"sentence": "The more he talked of his honor the faster we counted our spoons.", "length": 13},
    3: {"sentence": "Men are valued, not for what they are, but for what they seem to be.", "length": 15},
    4: {"sentence": "I do not pray for success. I ask for faithfulness.", "length": 10},
    5: {"sentence": "The farther a man knows himself to be from perfection, the nearer he is to it.", "length": 16},
    6: {"sentence": "Nearly all men can stand adversity, but if you want to test a man's character, give him power.", "length": 18},
    7: {"sentence": "When I examine myself and my methods of thought, I come to the conclusion that the gift of fantasy has meant more to me than my talent for absorbing positive knowledge.", "length": 31},
    8: {"sentence": "The great white is the most dangerous shark with a recorded 314 unprovoked attacks on humans.", "length": 16},
    9: {"sentence": "The Sun rotates in the opposite direction to Earth with the Sun rotating from west to east instead of east to west like Earth.", "length": 24},
    10: {"sentence": "Oranges in warmer regions like Vietnam and Thailand still stay green through maturity.", "length": 13}
}

def PickSentence():
    RandomSentence = random.randint(1,9)
    global SPEEDTEST_SENTENCE
    SPEEDTEST_SENTENCE = SENTENCES[RandomSentence]["sentence"]
    global SPEEDTEST_SENTENCE_WORDLENGTH
    SPEEDTEST_SENTENCE_WORDLENGTH = SENTENCES[RandomSentence]["length"]

def RefreshSentence():
    PickSentence()
    textLabel.configure(text=SPEEDTEST_SENTENCE)

def StartTimer():
    global START_TIME
    START_TIME = timer()

def CheckText(keyevent):
    if v.get() == SPEEDTEST_SENTENCE:
        END_TIME = timer()
        wordsPerMinute = round(((END_TIME - START_TIME) / SPEEDTEST_SENTENCE_WORDLENGTH) * 60, 1)
        global TopScore
        if wordsPerMinute >= TopScore:
            TopScore = wordsPerMinute
        SpeedLabel.configure(text=f"You hit {wordsPerMinute} words per minute!! Your top score so far is {TopScore}")
        SpeedEntry.delete(0, 'end')
        SpeedLabel.focus()
        PickSentence()
        textLabel.configure(text=SPEEDTEST_SENTENCE)

# Interface
TopScore = 0.0
window = Tk()
PickSentence()
window.title("Typing Speed Test")
window.config(padx=20, pady=20)
# Labels
instructionLabel = Label(text=f"Instructions:\n1. The timer will start when you click into the textbox below."
                              f"\n2. The timer will finish when you have typed the sentence EXACTLY as it appears below.\n\nYour sentence is:")
instructionLabel.grid(row=0, column=0)
global textLabel
textLabel = Label(text=SPEEDTEST_SENTENCE, font=("Arial", 14, "bold"), wraplength=500)
textLabel.grid(row=1, column=0)
global SpeedLabel
SpeedLabel = Label(text="Your speed result will appear here.")
SpeedLabel.grid(row=3, column=0, pady=20)
# Buttons
NewSentenceButton = Button(text="Change sentence...", command=RefreshSentence)
NewSentenceButton.grid(row=4, column=0, sticky="E")
# Inputs
global v
v = StringVar()
global SpeedEntry
SpeedEntry = Entry(width=80, justify="center", textvariable=v, validate="focusin", validatecommand=StartTimer)
SpeedEntry.grid(row=2, column=0, pady=10)
SpeedEntry.bind('<KeyRelease>', CheckText)

window.mainloop()