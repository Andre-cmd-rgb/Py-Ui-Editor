import tkinter as tk

def EditState(editstate):
        if editstate=="do":
                edit=True
        elif editstate=="stop":
                edit=False
        elif editstate=="what":
                if editstate=="do":
                        return True
                elif editstate=="stop":
                        return False
def EditScene(main):
        if EditState(main):
                return True
        if EditState(main)==False:
                return False


def screen():
        global window
        window=tk.Tk()
def addButtom(ButtomText=None,funcion=None):
        """add a buttom with text and funcion"""
        button = tk.Button(window, text=ButtomText, command = funcion).pack()
def addNumBox():
        """ add a num box"""
        global text
        text=tk.DoubleVar()
        text_box=tk.Entry(window,textvariable=text).pack()
def addTextBox(Height,Insert):
        TextBox=Text(window,height=Height)
        TextBox.pack()

def addlable():
        """add a label for float not for string"""
        global label
        label=tk.DoubleVar()
        label_box=tk.Label(window,textvariable=label).pack()
def mainsloop():
        window.mainloop()

#def menu(tetraroff):
class UI:
        def __init__(self):
                pass
        def addwindow():
                WindowUi=Window()

def textboxoutput():
        label.set(text.get())
        


