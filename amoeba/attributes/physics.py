#!/usr/bin/env python

from __future__ import division, absolute_import

import vector

class Position(vector.Vector):
    name = 'position'
    
class Velocity(vector.Vector):
    name = 'velocity'
    
class Acceleration(vector.Vector):
    name = 'acceleration'
    
class Radius(int):
    name = 'radius'
    