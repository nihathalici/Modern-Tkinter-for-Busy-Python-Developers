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

import re
def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5

check_num_wrapper = (root.register(check_num), '%P')

num = StringVar()
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid(column=0, row=0, sticky='we')

root.mainloop()