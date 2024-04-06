import random
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class AnimateGifLabel(Label):
    def __init__(self, *argv, image=None, **kwargs):
        self.master = argv[0]
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image=self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        # self.delay = 3 # Это минимально возможная задержка - иначе ткинтер не успевает обновится и не обновляет 2
        # (Но реагирует на события типа изменнения размера ) а при 1 даже не появляется
        self.after(self.delay, self.show_new_cadr)

    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames

    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i = 0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image=self.image)
        self.i += 1
        self.master.after(self.delay, self.show_new_cadr)



