import random
from queue import Queue
from tkinter import Tk, Canvas, Frame, BOTH, Button

from math import cos, sin, radians

import time

canvas_width = 1000
canvas_height = 1000
change_a = 20
start_length = 70
start_width = 10
start_delay = 50
left_branch_angle_change = 30
right_branch_angle_change = 30
left_branch_apear_chance = 90  # 0-100
right_branch_apear_chance = 90  # 0-100
flower_chance = 2
min_flower_size = 5  # >0
max_flower_size = 30  # >min_flower_size


class FractalTree(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.jobs = []
        self.delay = start_delay
        self.start_len = start_length
        self.shift = 0
        self.initUI()

    def initUI(self):
        self.parent.title("Fractal Tree")
        self.pack(fill=BOTH, expand=1)
        self.canvas = Canvas(self, width=canvas_width, height=canvas_height)
        b = Button(self.master, text="Redraw", command=self.redraw)
        b.pack()

        self.canvas.pack()
        self.canvas.create_line(canvas_width / 2, canvas_height - 100, canvas_width / 2, canvas_height, width=start_width)

        self.branch(self.start_len, canvas_width / 2, canvas_height - 100, line_width=start_width)

    def redraw(self):
        for job in self.jobs:
            self.after_cancel(job)
        self.jobs.clear()
        self.shift = 0
        self.canvas.delete('all')
        self.canvas.create_line(canvas_width / 2, canvas_height - 100, canvas_width / 2, canvas_height, width=start_width)
        self.branch(self.start_len, canvas_width / 2, canvas_height - 100, line_width=start_width)

    def branch(self, length, prevx, prevy, preva=-90, iteration=1, line_width=1):
        if length > 5 and line_width > 0:
            rn1 = random.randrange(left_branch_angle_change)
            rn2 = random.randrange(right_branch_angle_change)
            x1 = length * cos(radians(preva + change_a + rn1)) + prevx
            y1 = length * sin(radians(preva + change_a + rn1)) + prevy
            x2 = length * cos(radians(preva - change_a + rn2)) + prevx
            y2 = length * sin(radians(preva - change_a + rn2)) + prevy
            self.canvas.create_line(prevx, prevy, x1, y1, width=line_width)
            self.canvas.create_line(prevx, prevy, x2, y2, width=line_width)

            b_left_flower = False
            b_right_flower = False
            length -= 5
            iteration += 1
            line_width -= 1
            self.shift += 1

            if random.randrange(0, 100) > 100 - flower_chance:
                self.flower(x1, y1, preva + change_a + rn1)
                b_left_flower = True
            if random.randrange(0, 100) > 100 - flower_chance:
                self.flower(x2, y2, preva - change_a + rn2)
                b_right_flower = True


            if not b_left_flower and random.randrange(0, 100) > 100 - left_branch_apear_chance:
                self.jobs.append(self.after(self.delay + self.shift, self.branch, length, x1, y1, preva + change_a, iteration, line_width))
            if not b_right_flower and random.randrange(0, 100) > 100 - right_branch_apear_chance:
                self.jobs.append(self.after(self.delay, self.branch, length, x2, y2, preva - change_a, iteration, line_width))

    def flower(self, prevx, prevy, preva):
        flower_size = random.randrange(min_flower_size, max_flower_size)
        flower_petal_radius = flower_size
        for i in range(preva-50, preva+50, 20):
            x = flower_size * cos(radians(i)) + prevx
            y = flower_size * sin(radians(i)) + prevy
            self.canvas.create_oval(x - flower_petal_radius, y - flower_petal_radius, x + flower_petal_radius, y + flower_petal_radius, outline='red', width=2)
        self.canvas.create_oval(prevx - flower_size // 2, prevy - flower_size // 2, prevx + flower_size // 2, prevy + flower_size // 2, outline='green', fill='green')


root = Tk()
ex = FractalTree(root)
ex.mainloop()
