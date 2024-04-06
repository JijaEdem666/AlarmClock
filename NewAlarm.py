from tkinter import *
from tkinter import ttk
from datetime import datetime
from time import strftime


class NewAlarm:
    def __init__(self, master):
        self.master = master
        self.top = Toplevel(self.master)
        self.top.title("Добавление будильника")
        self.top.geometry("500x500")

        label = Label(self.top, text="Выберите тип уведомления:", font=("Arial", 11))
        label.place(x=150, y=20)

        f = lambda t="event": self.create_alarm(t)
        button_event = Button(self.top, text="Важное событие", font=("Arial", 11), command=f)
        button_event.place(x=150, y=100)

        f = lambda t="daily": self.create_alarm(t)
        button_alarm1 = Button(self.top, text="Будильник на каждый день", font=("Arial", 11), command=f)
        button_alarm1.place(x=150, y=150)

        f = lambda t="weekly": self.create_alarm(t)
        button_alarm2 = Button(self.top, text="Будильник на дни недели", font=("Arial", 11), command=f)
        button_alarm2.place(x=150, y=200)

        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()

    def create_alarm(self, t):
        self.top.destroy()
        self.top = Toplevel(self.master)
        self.top.geometry("500x200")
        if t == "event":
            label = Label(self.top, text="Установите дату:", font=("Arial", 11))
            label.place(x=50, y=20)

            year = StringVar(value=str(strftime("%Y")))
            year_box = ttk.Spinbox(self.top, from_=float(strftime("%Y")), to=float(strftime("%Y")) + 70, increment=1, state="readonly", textvariable=year)
            year_box.place(x=10, y=60)

            months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
                      "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
            month = StringVar(value=months[0])
            month_box = ttk.Combobox(self.top, textvariable=month, values=months, state="readonly")
            month_box.place(x=170, y=60)

            day = StringVar(value="1")
            day_box = ttk.Spinbox(self.top, from_=1, to=31, increment=1, state="readonly", textvariable=day)
            day_box.place(x=330, y=60)

            label_event = Label(self.top, text="Название события:")
            label_event.place(x=50, y=100)
            entry_event = ttk.Entry(self.top, width=50)
            entry_event.place(x=50, y=130)

            button_add = Button(self.top, text="Добавить событие", font=("Arial", 11))
            button_add.place(x=160, y=160)



        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()
