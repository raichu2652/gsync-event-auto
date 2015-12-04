#!/usr/bin/env python

import gtk, pygtk
import time
from math import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard

def distance(p1, p2):
    return sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2))

def click(p, t = 0.6):
    x = p.x
    y = p.y
    m = PyMouse()
    m.move(x, y)
    m.click(x, y, 1)
#    m.press(x, y)
#    m.release(x, y)
    time.sleep(t)

def drag(p1, p2, t = 0.05):
    m = PyMouse()
    m.press(p1.x, p1.y, 1)

    x = p1.x
    y = p1.y
    step = 5
    while distance(Point(x, y), p2) >= 1 :
        x += (p2.x - x)/step
        y += (p2.y - y)/step
        step -= 1
        m.drag(x, y)
#        time.sleep(0.01)
    m.release(p2.x, p2.y, 1)
    time.sleep(t)

def enter(t = 0.175):
    k = PyKeyboard()
    k.tap_key(k.return_key)
    time.sleep(t)

def select(p):

class Point:
    ''' Creates a point on a coordinate plane with x and y values '''

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

# UI points
x_dim, y_dim = PyMouse().screen_size()
p_start = Point(683, 573)
p_gsync = Point(1254, 695)
p_resume = Point(686, 420)

# Drag points
p_drag_middle = Point(x_dim/2, y_dim/2)
p_drag_left = Point(100, y_dim/2)
p_drag_right = Point(x_dim - 100, y_dim/2)
p_drag_up = Point(x_dim/2, 100)
p_drag_down = Point(x_dim/2, y_dim - 100)

# Target points in the middle area
p_target_mid = [Point(386, 261), Point(798,259), Point(1053, 181)]
p_target_left = [Point(455, 70), Point(417, 97), Point(852, 174), Point(851, 246), Point(882, 254), Point(976, 593)]
p_target_r = [Point(281, 618), Point(504, 339), Point(904, 239), Point(811, 447)]

time.sleep(1.5)
enter(0.45)
# click(p_gsync)

# middle screen characters
click(p_target_mid[0])
enter()
click(p_target_mid[1])
enter()
click(p_target_mid[2])
enter()

for i in range(13):

# drag screen to left
drag(p_drag_left, p_drag_middle)
