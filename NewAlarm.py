from tkinter import *
from tkinter import ttk
from time import strftime
from alarm_list import alarm_list


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
        button_alarm2 = Button(self.top, text="Будильник на день недели", font=("Arial", 11), command=f)
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

            event_name = StringVar()
            entry_event = ttk.Entry(self.top, width=50, textvariable=event_name)
            entry_event.place(x=50, y=130)

            f = lambda n=event_name, y=year, m=month, d=day: self.add_event(n, y, m, d)
            button_add = Button(self.top, text="Добавить событие", font=("Arial", 11), command=f)
            button_add.place(x=160, y=160)
        elif t == "daily":
            label = Label(self.top, text="Установите время будильника:", font=("Arial", 11))
            label.place(x=500/2, y=20, anchor=N)

            hour = StringVar(value="0")
            label_hour = Label(self.top, text="Часы:")
            label_hour.place(x=50, y=60)
            hours = ttk.Spinbox(self.top, textvariable=hour, from_=0, to=23, increment=1, state="readonly")
            hours.place(x=100, y=60)

            minute = StringVar(value="0")
            label_minute = Label(self.top, text="Минуты:")
            label_minute.place(x=260, y=60)
            minutes = ttk.Spinbox(self.top, textvariable=minute, from_=0, to=59, increment=1, state="readonly")
            minutes.place(x=320, y=60)

            f = lambda h=hour, m=minute: self.add_daily(h, m)
            button_add = Button(self.top, text="Добавить будильник", font=("Arial", 11), command=f)
            button_add.place(x=250, y=160, anchor=N)
        elif t == "weekly":
            label = Label(self.top, text="Установите время и день недели:", font=("Arial", 11))
            label.place(x=500 / 2, y=20, anchor=N)

            hour = StringVar(value="0")
            label_hour = Label(self.top, text="Часы:")
            label_hour.place(x=50, y=60)
            hours = ttk.Spinbox(self.top, textvariable=hour, from_=0, to=23, increment=1, state="readonly")
            hours.place(x=100, y=60)

            minute = StringVar(value="0")
            label_minute = Label(self.top, text="Минуты:")
            label_minute.place(x=260, y=60)
            minutes = ttk.Spinbox(self.top, textvariable=minute, from_=0, to=59, increment=1, state="readonly")
            minutes.place(x=320, y=60)

            day = StringVar(value="Понедельник")
            days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
            label_day = Label(self.top, text="День недели:")
            label_day.place(x=50, y=100)
            day_box = ttk.Combobox(self.top, textvariable=day, values=days, state="readonly")
            day_box.place(x=130, y=100)

            f = lambda h=hour, m=minute, d=day: self.add_weekly(h, m, d)
            button_add = Button(self.top, text="Добавить будильник", font=("Arial", 11), command=f)
            button_add.place(x=250, y=160, anchor=N)

        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()

    def add_event(self, event_name, year, month, day):
        alarm_list.append(["event", event_name, year, month, day])
        self.top.destroy()

    def add_daily(self, hour, minute):
        alarm_list.append(["daily", hour, minute])
        self.top.destroy()

    def add_weekly(self, hour, minute, day):
        alarm_list.append(["weekly", hour, minute, day])
        self.top.destroy()
