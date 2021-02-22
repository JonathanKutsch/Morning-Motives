import tkinter
import random
from tkinter import font

window = tkinter.Tk()

window.title("Morning Motives")

phrases = [
    "It’s either “Day One” or “One Day”... it’s your choice. ",
    "Becoming is better than being.",
    "Performance cannot be measured by one assessment. You can not determine the slop of a line with one point, as there is no line to begin with. A single point in time does not show trends.",
    "Do not let an action turn into an identity. Failing does not make you a failure. Losing does not make you a loser.",
    "You aren’t a failure until you start to blame",
    "Success is about being your best self, not about being better than others; failure is an opportunity, not a condemnation; effort is the key to success.",
    "It’s tempting to create a world in which we are perfect. Do not surround yourself with people that make you feel faultless. Next time you’re tempted to surround yourself with worshippers, go to church. In the rest of your life, seek constructive criticism.",
    "Character: being able to dig down and find the strength even when things are going against you. Ability gets you to the top, character is what keeps you there.",
    "The best way to live a life of purpose is to live on purpose.",
    "Lesson: do not live for validation from others",
    "Sorrow looks down. Worry looks around. Faith looks up.",
    "You must accept your limits in order to go beyond them.",
    "If you can’t fly, then run. If you can’t run, then walk. If you can’t walk, then crawl. Whatever you do, keep moving forward.",
    "Don’t judge. Teach. It’s a learning process.",
    "If you don’t do it, Someone else will. Don’t let that happen.",
    "Take the risk or lose the chance."
    "Be a good person, but don’t waste ur time proving it.",
    "Don’t choose comfort over progress.",
    "Goals without deadlines aren’t goals; they’re merely directions.",
    "Don’t be scared to die, because you are fortunate to live.",
    "You have to get off the boat in order to walk on water. Take the risk.",
    "You can’t capitalize on the present if you’re stuck in the past."
]

def give_me_motivation():
    tkinter.Label(window, text = random.choice(phrases), font='30').pack()

tkinter.Label(window, text = "Good Morning!", font="100").pack()
tkinter.Button(window, text = "Click Me Motivation", font="50", fg='blue', command = give_me_motivation).pack()
window.mainloop()
