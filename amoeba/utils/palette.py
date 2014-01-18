#!/usr/bin/env python

from __future__ import division, absolute_import

class Color(object):
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