from tkinter import *
from Watch import Watch
from AlarmRoot import AlarmRoot


class MainRoot:

    def __init__(self):
        self.root = Tk()
        self.root.geometry("700x700")
        self.root.title("Будильник")
        self.root.resizable(False, False)
        watch = Watch(self.root)

        button_alarm = Button(text="Настроить будильник", font=("Arial", 15), command=self.open_alarm)
        button_alarm.pack(pady=20)

    def mainloop(self):
        self.root.mainloop()

    def open_alarm(self):
        alarm_menu = AlarmRoot(self.root)