from queue import Queue
from tkinter import Tk, Canvas, Frame, BOTH

from math import cos, sin, radians

import time

canvas_width = 1000
canvas_height = 1000
change_a = 20
start_length = 70

class FractalTree(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.delay = 50
        self.start_len = start_length
        self.shift = 0
        self.initUI()

    def initUI(self):
        self.parent.title("Fractal Tree")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=canvas_width, height=canvas_height)
        self.canvas.pack()
        self.canvas.create_line(canvas_width / 2, canvas_height - 100, canvas_width / 2, canvas_height)

        self.branch(self.start_len, canvas_width / 2, canvas_height - 100)

    def branch(self, length, prevx, prevy, preva=-90, iteration=1):
        if length > 5:
            x1 = length * cos(radians(preva + change_a)) + prevx
            y1 = length * sin(radians(preva + change_a)) + prevy
            x2 = length * cos(radians(preva - change_a)) + prevx
            y2 = length * sin(radians(preva - change_a)) + prevy
            self.canvas.create_line(prevx, prevy, x1, y1)
            self.canvas.create_line(prevx, prevy, x2, y2)
            self.shift += 1
            length -= 5
            iteration += 1

            self.after(self.delay + self.shift, self.branch, length, x1, y1, preva + change_a, iteration)
            self.after(self.delay, self.branch, length, x2, y2, preva - change_a, iteration)


root = Tk()
ex = FractalTree(root)
ex.mainloop()
