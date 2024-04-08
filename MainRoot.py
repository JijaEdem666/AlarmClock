from tkinter import *
from Watch import Watch
from AlarmRoot import AlarmRoot
from Fun import Fun
from alarm_list import alarm_list
from time import strftime


class MainRoot:

    def __init__(self):
        self.root = Tk()
        self.alarm_menu = None
        x = 0
        y = (self.root.winfo_screenheight() - 700) / 2
        self.root.wm_geometry("+%d+%d" % (x, y))
        self.root.geometry("700x700")
        self.root.title("Будильник")
        self.root.resizable(False, False)
        watch = Watch(self.root)

        button_alarm = Button(text="Настроить будильник", font=("Arial", 15), command=self.open_alarm)
        button_alarm.pack(pady=20)
        self.check_alarms()
        self.root.mainloop()


    def open_alarm(self):
        self.alarm_menu = AlarmRoot(self.root)
        self.alarm_menu.mainloop()

    def fun(self):
        Fun(self.root)

    def check_alarms(self):
        for i in range(len(alarm_list)):
            if alarm_list[i][0] == "event":
                match strftime("%B"):
                    case "January":
                        month_string = "Январь"
                    case "February":
                        month_string = "Февраль"
                    case "March":
                        month_string = "Март"
                    case "April":
                        month_string = "Апрель"
                    case "May":
                        month_string = "Май"
                    case "June":
                        month_string = "Июнь"
                    case "July":
                        month_string = "Июль"
                    case "August":
                        month_string = "Август"
                    case "September":
                        month_string = "Сентябрь"
                    case "October":
                        month_string = "Октябрь"
                    case "November":
                        month_string = "Ноябрь"
                    case "December":
                        month_string = "Декабрь"
                if (strftime("%Y") == alarm_list[i][2].get()) & (month_string == alarm_list[i][3].get()) & (str(int(strftime("%d"))) == alarm_list[i][4].get()):
                    fun = Fun(self.root, i, self.alarm_menu, "event")
            elif alarm_list[i][0] == "daily":
                if (str(int(strftime("%H"))) == alarm_list[i][1].get()) & (str(int(strftime("%M"))) == alarm_list[i][2].get()) & (str(int(strftime("%S"))) == "0"):
                    fun = Fun(self.root, i, self.alarm_menu, "daily")
            elif alarm_list[i][0] == "weekly":
                day = ""
                match alarm_list[i][3].get():
                    case "Понедельник":
                        day = "Monday"
                    case "Вторник":
                        day = "Tuesday"
                    case "Среда":
                        day = "Wednesday"
                    case "Четверг":
                        day = "Thursday"
                    case "Пятница":
                        day = "Friday"
                    case "Суббота":
                        day = "Saturday"
                    case "Воскресенье":
                        day = "Sunday"
                if (str(int(strftime("%H"))) == alarm_list[i][1].get()) & (
                        str(int(strftime("%M"))) == alarm_list[i][2].get()) & (str(int(strftime("%S"))) == "0") & (strftime("%A") == day):
                    fun = Fun(self.root, i, self.alarm_menu, "weekly")

        self.root.after(1000, self.check_alarms)