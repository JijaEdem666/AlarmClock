from tkinter import *

class AlarmRoot:

    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.geometry("700x700")
        self.top.title("Настройка будильника")
        button_add = Button(self.top, text="Установить будильник", font=("Arial", 12))
        button_add.pack()
        canvas = Canvas(self.top, bg="white")
        canvas.create_text(700//2, 0, text="Пока будильников нет")
        canvas.pack(expand=True)
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()