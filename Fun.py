from tkinter import *
from PIL import ImageTk, Image
import random
from AnimateGifLabel import *
from pygame import mixer



class Fun:

    def __init__(self, root):
        self.top = Toplevel(root)
        x = self.top.winfo_screenwidth() - 700
        y = (self.top.winfo_screenheight() - 700) / 2
        self.top.wm_geometry("+%d+%d" % (x, y))
        self.top.title("WAKE UP")

        imageList = ["gifs/gif_1.gif",
                     "gifs/gif_2.gif",
                     "gifs/gif_3.gif",
                     "gifs/gif_4.gif"]

        soundsList = ["sounds/sound_1.mp3",
                      "sounds/sound_2.mp3",
                      "sounds/sound_3.mp3"]

        AnimateGifLabel(self.top, image=imageList[random.randint(0, 3)]).pack(expand=True)

        #label = Label(self.top, height=200, width=200, image=imageList[random.randint(0, 3)])
        #label.pack(expand=True)

        mixer.init()
        mixer.music.load(soundsList[random.randint(0, 2)])

        mixer.music.play(-1)

        self.button_stop = Button(self.top, text="СТОП")
        self.button_stop["command"] = self.button_clicked
        self.button_stop.pack(anchor="center", expand=1)

        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()



    def button_clicked(self):
        mixer.music.stop()
        self.top.destroy()






