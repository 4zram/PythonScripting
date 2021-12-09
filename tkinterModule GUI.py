"""
This will output a GUI window with the configured buttons.
"""
import tkinter

from tkinter import Tk
from tkinter import ttk
from tkinter import *

root=Tk()
root.title("First GUI using python")
ttk.Button(root, text="Hello Buddy!").grid()
root.mainloop()