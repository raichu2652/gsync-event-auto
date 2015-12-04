#!/usr/bin/env python

import gtk, pygtk
import time
from math import *
from pymouse import PyMouse
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()

def enter(t = 0.15):
    k = PyKeyboard()
    k.tap_key(k.return_key)
    time.sleep(t)

def select(p, t1 = 0.6):
    x = p.x / 3
    y = p.y / 3
    m.move(x, y)
    for i in range(10):
        m.click(x, y, 1)
        time.sleep(0.005)
    time.sleep(t1)
    enter()


class Point:
    ''' Creates a point on a coordinate plane with x and y values '''

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

target = [Point(2423, 789), Point(2165, 1030), Point(1762, 1036),
          Point(1201, 861), Point(1240, 843), Point(1639, 1396), Point(1639, 1471), Point(1669, 1477),
          Point(1765, 1816), Point(2231, 1903), Point(2456, 1624), Point(2768, 1237), Point(2861, 1009)]

time.sleep(1.5)
enter(0.5)
# click(p_gsync)

select(target[0])
select(target[1])
select(target[2])
select(target[3])
select(target[4])
select(target[5])
select(target[6])
select(target[7])
select(target[8])
select(target[9])
select(target[10])
select(target[11])
select(target[12])
