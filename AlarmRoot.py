from tkinter import *
from NewAlarm import NewAlarm

class AlarmRoot:

    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.geometry("700x700")
        self.top.title("Настройка будильника")
        button_add = Button(self.top, text="Установить будильник", font=("Arial", 12), command=self.create_alarm)
        button_add.pack()
        canvas = Canvas(self.top, bg="white", width=600, height=600)
        canvas.create_text(600//2, 20, text="Пока будильников нет")
        canvas.pack()
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()

    def create_alarm(self):
     new_alarm = NewAlarm(self.top)
