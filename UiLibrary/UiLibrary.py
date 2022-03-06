import tkinter as tk
Ui=[]
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
class UIEdit:
        def __init__(UiName):
                UiNum=None
                Ui.append(UiName)
                Ui.append(UiNum)


def screen():
        global window
        window=tk.Tk()
def addButtom(ButtomText=None,funcion=None):
        button = tk.Button(window, text=ButtomText, command = funcion)
        button.pack()

class UI:
        def __init__(self):
                pass
        def addwindow():
                WindowUi=Window()


