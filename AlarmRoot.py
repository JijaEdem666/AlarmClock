from tkinter import *
from tkinter import ttk
from NewAlarm import NewAlarm
from alarm_list import alarm_list

class AlarmRoot:

    def __init__(self, root):
        self.top = Toplevel(root)
        self.top.geometry("700x700")
        self.top.title("Настройка будильника")
        button_add = Button(self.top, text="Установить будильник", font=("Arial", 12), command=self.create_alarm)
        button_add.pack()
        self.canvas = Canvas(self.top, bg="white", width=600, height=600)
        self.canvas.pack(side=LEFT, fill=BOTH)
        self.scrollbar = Scrollbar(self.top, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.update()

    def mainloop(self):
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()

    def create_alarm(self):
        new_alarm = NewAlarm(self.top)
        self.update()

    def update(self):
        self.canvas.delete("all")
        if len(alarm_list) == 0:
            self.canvas.create_text(600/2, 20, text="Пока будильников нет")
        else:

            x = 20
            y = 20
            for i in range(len(alarm_list)):
                if alarm_list[i][0] == "event":
                    self.canvas.create_text(x, y, text=alarm_list[i][1].get(), anchor=NW, font=("Arial", 10))
                    f = lambda x=i: self.delete_alarm(x)
                    btn_del = Button(self.canvas, text="Удалить будильник", font=("Arial", 9), command=f)
                    self.canvas.create_window(x + 420, y-5, anchor=NW, window=btn_del)
                    f = lambda x=i: self.check_event(x)
                    btn_check = Button(self.canvas, text="Посмотреть информацию", font=("Arial", 9), command=f)
                    self.canvas.create_window(x + 220, y-5, anchor=NW, window=btn_check)
                elif alarm_list[i][0] == "daily":
                    self.canvas.create_text(x, y, text="Ежедневный будильник", font=("Arial", 9), anchor=NW)

                    h = alarm_list[i][1].get()
                    m = alarm_list[i][2].get()
                    if (int(h) < 10):
                        h = "0" + h
                    if (int(m) < 10):
                        m = "0" + m

                    self.canvas.create_text(x + 220, y, text=h + ":" + m, anchor=NW, font=(("Arial"), 10))
                    f = lambda x=i: self.delete_alarm(x)
                    btn_del = Button(self.canvas, text="Удалить будильник", font=("Arial", 9), command=f)
                    self.canvas.create_window(x + 420, y - 5, anchor=NW, window=btn_del)
                elif alarm_list[i][0] == "weekly":
                    label_day = ""
                    match alarm_list[i][3].get():
                        case "Понедельник":
                            label_day = "Понедельник"
                        case "Вторник":
                            label_day = "Вторник"
                        case "Среда":
                            label_day = "Среду"
                        case "Четверг":
                            label_day = "Четверг"
                        case "Пятница":
                            label_day = "Пятницу"
                        case "Суббота":
                            label_day = "Субботу"
                        case "Воскресенье":
                            label_day = "Воскресенье"
                    self.canvas.create_text(x, y, text="Будильник на " + label_day, font=("Arial", 9), anchor=NW)

                    h = alarm_list[i][1].get()
                    m = alarm_list[i][2].get()
                    if (int(h) < 10):
                        h = "0" + h
                    if (int(m) < 10):
                        m = "0" + m

                    self.canvas.create_text(x + 220, y, text=h + ":" + m, anchor=NW,
                                            font=(("Arial"), 10))
                    f = lambda x=i: self.delete_alarm(x)
                    btn_del = Button(self.canvas, text="Удалить будильник", font=("Arial", 9), command=f)
                    self.canvas.create_window(x + 420, y - 5, anchor=NW, window=btn_del)

                y += 40
        self.canvas.configure(scrollregion=self.canvas.bbox('all'), yscrollcommand=self.scrollbar.set)

    def delete_alarm(self, i):
        alarm_list.pop(i)
        self.update()

    def check_event(self, i):
        info = Toplevel(self.top)
        info.geometry("400x200")
        info.title("Информация о будильнике")
        label_event = Label(info, text="Важное событие", font=("Arial", 12))
        label_event.place(x=200, y=20, anchor=N)
        label_date = Label(info, text="Дата: " + alarm_list[i][4].get() + " " + alarm_list[i][3].get() + " " + alarm_list[i][2].get(), font=("Arial", 10))
        label_date.place(x=200, y=100, anchor=N)
        label_name = Label(info, text=alarm_list[i][1].get(), font=("Arial", 10))
        label_name.place(x=200, y=60, anchor=N)
        info.grab_set()
        info.focus_set()
        info.wait_window()
