from sys import exit
try:
    from tkinter import Tk
except ImportError:
    print("tkinter did not import successfully. Please check your setup.")
    exit(1)

from .ui import ui



