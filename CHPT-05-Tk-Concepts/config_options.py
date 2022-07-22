"""by Mark Roseman
   mark@markroseman.com

   View this code at
   https://github.com/roseman/tkdocs/
   or
   https://tkdocs.com/
"""

from tkinter import *
from tkinter import ttk

root = Tk()

# create a button, passing two options
button = ttk.Button(root, text="Hello", command=buttonpressed)
button.grid()

# check the current value of the text option:
button['text']

# change the value of the text option:
button['text'] = 'goodbye'

# another way to do the same thing:
button.configure(text='goodbye')

# check the current value of the text option:
button['text']

# get all information about the text option:
button.configure('text')

# get information on all options for this widget:
button.configure()
