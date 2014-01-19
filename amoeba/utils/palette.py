#!/usr/bin/env python

from __future__ import division, absolute_import

class RGB(object):
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        
    @property
    def rgb(self):
        return (self.r, self.g, self.b)
        
    @rgb.setter
    def set_rgb(self, rgb):
        self.r, self.g, self.b = rgb

    def __add__(self, other):
        tup = other
        if type(other) == RGB:
            tup = other.rgb
        return RGB(self.r + other[0],self.g + other[1],self.b + other[2])

    def __sub__(self, other):
        tup = other
        if type(other) == RGB:
            tup = other.rgb
        return self.__add__((-tup[0], -tup[1], -tup[2]))

BLUE = RGB(0, 0, 255)
RED = RGB(255, 0, 0)
GREEN = RGB(0, 255, 0)
PINK = RGB(255, 51, 255)
ORANGE = RGB(255, 128, 0)
YELLOW = RGB(255, 255, 0)
LIGHT_BLUE = RGB(0, 255, 255)