import tkinter as tk
from datetime import datetime
from time import strftime
import math


class Watch:
    def __init__(self, root):
        self.root = root

        self.CLOCK_WIDTH = 400
        self.CLOCK_HEIGHT = 400
        self.CLOCK_CENTER_X = self.CLOCK_WIDTH // 2
        self.CLOCK_CENTER_Y = self.CLOCK_HEIGHT // 2
        self.CLOCK_RADIUS = min(self.CLOCK_WIDTH, self.CLOCK_HEIGHT) // 2 - 20

        self.CLOCK_RAST = 15  # Расстояние между аналоговыми и цифровыми часами

        self.canvas = tk.Canvas(self.root, width=self.CLOCK_WIDTH, height=self.CLOCK_HEIGHT, bg="white")
        self.canvas.pack(side=tk.TOP, pady=self.CLOCK_RAST)

        self.clock_label = tk.Label(self.root, bg="black", fg="white", font=("Arial", 30, 'bold'), relief='flat')
        self.clock_label.pack(side=tk.TOP)

        self.draw_clock()
        self.update_label()

    def draw_clock(self):
        current_time = datetime.now()
        hour = current_time.hour
        minute = current_time.minute
        second = current_time.second

        self.canvas.delete("all")
        self.canvas.create_oval(self.CLOCK_CENTER_X - self.CLOCK_RADIUS, self.CLOCK_CENTER_Y - self.CLOCK_RADIUS,
                                self.CLOCK_CENTER_X + self.CLOCK_RADIUS, self.CLOCK_CENTER_Y + self.CLOCK_RADIUS, width=5)

        hour_angle = math.radians((hour % 12) * 30 - 90)
        hour_x = self.CLOCK_CENTER_X + 0.6 * self.CLOCK_RADIUS * math.cos(hour_angle)
        hour_y = self.CLOCK_CENTER_Y + 0.6 * self.CLOCK_RADIUS * math.sin(hour_angle)
        self.canvas.create_line(self.CLOCK_CENTER_X, self.CLOCK_CENTER_Y, hour_x, hour_y, width=4)

        minute_angle = math.radians(minute * 6 - 90)
        minute_x = self.CLOCK_CENTER_X + 0.8 * self.CLOCK_RADIUS * math.cos(minute_angle)
        minute_y = self.CLOCK_CENTER_Y + 0.8 * self.CLOCK_RADIUS * math.sin(minute_angle)
        self.canvas.create_line(self.CLOCK_CENTER_X, self.CLOCK_CENTER_Y, minute_x, minute_y, width=3)

        second_angle = math.radians(second * 6 - 90)
        second_x = self.CLOCK_CENTER_X + 0.9 * self.CLOCK_RADIUS * math.cos(second_angle)
        second_y = self.CLOCK_CENTER_Y + 0.9 * self.CLOCK_RADIUS * math.sin(second_angle)
        self.canvas.create_line(self.CLOCK_CENTER_X, self.CLOCK_CENTER_Y, second_x, second_y, fill="red", width=2)

        self.canvas.create_oval(self.CLOCK_CENTER_X - 5, self.CLOCK_CENTER_Y - 5, self.CLOCK_CENTER_X + 5, self.CLOCK_CENTER_Y + 5, fill="black")

        self.canvas.after(1000, self.draw_clock)

    def update_label(self):
        current_time = strftime('%H:%M:%S')
        match strftime("%A"):
            case "Monday":
                day_string = "Понедельник"
            case "Tuesday":
                day_string = "Вторник"
            case "Wednesday":
                day_string = "Среда"
            case "Thursday":
                day_string = "Четверг"
            case "Friday":
                day_string = "Пятница"
            case "Saturday":
                day_string = "Суббота"
            case "Sunday":
                day_string = "Воскресенье"
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
        date_string = strftime(" %d, %Y")
        self.clock_label.config(text=current_time + "\n" + day_string + "\n" + month_string + date_string)
        self.clock_label.after(1000, self.update_label)
