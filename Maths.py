from tkinter import *
from math import *

master = Tk()
# master.iconbitmap(r'root.ico')
master.resizable(0, 0)
master.wm_title('\u221a Square')

Label(master, text='\u221a x').grid(row=0, column=0)
Label(master, text='Guesses').grid(row=1, column=0)
Label(master, text='Tolerance').grid(row=2, column=0)
Label(master, text='Lower Bound').grid(row=3, column=0)
Label(master, text='Upper Bound').grid(row=4, column=0)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.insert(0, 2)
e2.insert(0, 100)
e3.insert(0, 0)
e4.insert(0, 0)
e5.insert(0, 2)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

v = StringVar()
Label(
	master,
	textvariable=v,
	height=3,
	width=44,
	font='Verdana 10 bold',
	bg='white',
	).grid(row=6, column=0, columnspan=2)

def find_root(event=None):
    try:
        x = float(e1.get())
    except ValueError:
        output = \
            '''I\'m sorry. 
I can\'t find the square root of words/letters. 
Please enter a number instead.'''

        v.set(output)
        return
    if x == 0:
        output = \
            'The square root of 0 is: 0. \nThe uncertainty (%) is: 0'

        v.set(output)
        return
    elif x < 0:
        output = \
            '''This is unfortunate. 
I am still relatively new to imaginary numbers. 
I cannot process negative numbers at the moment.'''

        v.set(output)
    try:
        numGuesses = int(e2.get())
    except ValueError:
        output = \
            '''I\'m sorry. 
I can\'t process Guesses like that at the moment. 
Sorry for the inconvenience.'''

        v.set(output)
        return
    if numGuesses == 0 or numGuesses < 0:
        output = \
            'Please enter a positive value larger than 0. \nRegrettably I cannot process in the 4th dimension.'

        v.set(output)
        return
    Guesses = 0
    try:
        Tolerance = float(e3.get())
    except ValueError:
        output = \
            '''Not to be rude. 
Do you know what tolerance even means? 
Please look it up before using me.'''

        v.set(output)
        return
    if Tolerance < 0:
        output = \
            '''You are a truly unique user. 
I am honoured that you believe I am capable 
of traversing through the fourth dimension!'''

        v.set(output)
        return
    try:
        Lower = float(e4.get())
    except ValueError:
        output = 'Please, stop using me in unconventional methods.'

        v.set(output)
        return
    try:
        Upper = float(e5.get())
    except ValueError:
        output = \
            'I\'m convinced now that you are a baby. \nGoo goo ga ga'

        v.set(output)
        return
    Answer = (Upper + Lower) / 2.0

    while abs((Upper - Lower) / 2.0) > Tolerance and Answer ** 2 != x \
        and Guesses != numGuesses:
        Guesses += 1
        if Answer ** 2 < x:
            Lower = Answer
            Answer = (Upper + Lower) / 2.0
        else:
            Upper = Answer
            Answer = (Upper + Lower) / 2.0

    Uncertainty = abs(Answer - sqrt(x)) / sqrt(x) * 100

    output = \
        'The square root of {0} is: {1}. \nThe uncertainty (%) is: {2}'.format(x,
            Answer, Uncertainty)

    v.set(output)

master.bind('<Return>', find_root)
Button(master, text='Calculate', command=find_root).grid(row=7, column=0,
        sticky=W, pady=4, padx=4)
Button(master, text='Quit', command=master.quit).grid(row=7, column=1,
        sticky=E, pady=4, padx=4)

master.mainloop()	