import sys
import tkinter as tk


class Renderer:
    def __init__(self, w, h, title='Title'):
        self.root = tk.Tk()

        self.width = w  # self.root.winfo_screenwidth()
        self.height = h  # self.root.winfo_screenheight()

        # self.root.overrideredirect(True)
        # self.root.geometry("{0}x{1}+0+0".format(self.width, self.height))

        self.origin_x = self.width / 2
        self.origin_y = self.height / 2
        self.is_running = True
        self.frame = 0
        self.title = title

        self.root.focus_set()
        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height,
            borderwidth=0, highlightthickness=0, bg='#0B1014'
        )
        self.root.bind('<Escape>', lambda e: self._exit())

        # self.canvas.grid()
        self.canvas.pack()

    def destroy(self):
        self.root.destroy()

    def update(self):
        self.frame += 1
        self.root.title(self.title + ' : ' + str(self.frame))

        self.root.update()
        self.canvas.delete('all')

    def arc(self, x, y, r, **kwargs):
        x, y = self._origin_translate(x, y)
        self.canvas.create_oval(
            x - r, y - r, x + r, y + r, **kwargs
        )

    def line(self, x_f, y_f, x_t, y_t, **kwargs):
        x_f, y_f = self._origin_translate(x_f, y_f)
        x_t, y_t = self._origin_translate(x_t, y_t)

        self.canvas.create_line(
            x_f, y_f, x_t, y_t, **kwargs
        )

    def text(self, x, y, **kwargs):
        x, y = self._origin_translate(x, y)
        self.canvas.create_text(
            x, y, **kwargs
        )

    def _exit(self):
        self.is_running = False

    def _origin_translate(self, x, y):
        return self.origin_x + x, self.origin_y - y
