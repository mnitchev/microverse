import sys
import time
from tkinter import *


class Renderer:
    def __init__(self, w, h):
        self.tk = Tk()

        self.width = w  # self.tk.winfo_screenwidth()
        self.height = h  # self.tk.winfo_screenheight()
        self.origin_x = self.width / 2
        self.origin_y = self.height / 2

        # self.tk.overrideredirect(True)
        # self.tk.geometry("{0}x{1}+0+0".format(self.tk.winfo_screenwidth(),
                                            #   self.tk.winfo_screenheight()))

        self.tk.focus_set()
        self.canvas=Canvas(self.tk, width=self.width, height=self.height,
                           borderwidth=0, highlightthickness=0, bg='white')
        self.tk.bind("<Escape>", lambda e: sys.exit())
        self.tk.title('Title')

        # self.canvas.grid()
        self.canvas.pack()

    def update(self):
        self.tk.update()
        self.canvas.delete('all')

    def arc(self, x, y, r, **kwargs):
        x, y=self.origin_translate(x, y)
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r, **kwargs
        )

    def line(self, x_f, y_f, x_t, y_t, **kwargs):
        x_f, y_f = self.origin_translate(x_f, y_f)
        x_t, y_t = self.origin_translate(x_t, y_t)
        
        self.canvas.create_line(
            x_f, y_f, x_t, y_t, **kwargs
        )

    def origin_translate(self, x, y):
        return self.origin_x + x, self.origin_y - y
