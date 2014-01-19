#!/usr/bin/env python

from __future__ import division, absolute_import

from utils.vector import *

class Position(Vector):
    name = 'position'

class Circles(list):
    name = 'circles'
    
class Friction(float):
    name = 'friction'