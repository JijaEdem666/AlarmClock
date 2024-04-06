from tkinter import *
from Watch import Watch
from AlarmRoot import AlarmRoot
from Fun import Fun


class MainRoot:

    def __init__(self):
        self.root = Tk()
        x = 0
        y = (self.root.winfo_screenheight() - 700) / 2
        self.root.wm_geometry("+%d+%d" % (x, y))
        self.root.geometry("700x700")
        self.root.title("Будильник")
        self.root.resizable(False, False)
        watch = Watch(self.root)

        button_alarm = Button(text="Настроить будильник", font=("Arial", 15), command=self.open_alarm)
        button_alarm.pack(pady=20)
        self.fun()

    def mainloop(self):
        self.root.mainloop()

    def open_alarm(self):
        alarm_menu = AlarmRoot(self.root)

    def fun(self):
        Fun(self.root)
