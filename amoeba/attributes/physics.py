#!/usr/bin/env python

from __future__ import division, absolute_import

from utils.vector import *

class Position(Vector):
    name = 'position'
    
class Velocity(Vector):
    name = 'velocity'
    
class Acceleration(Vector):
    name = 'acceleration'
    
class Radius(int):
    name = 'radius'
    