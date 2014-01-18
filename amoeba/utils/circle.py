#!/usr/bin/env python

from __future__ import division, absolute_import

from utils.vector import *

class Circle(object):
    def __init__(self, position, velocity, radius):
        self.position = position
        self.velocity = velocity
        self.acceleration = Vector(0, 0)
        self.radius = radius
        
    def is_intersecting(self, other):
        min_distance = self.radius - other.radius
        actual_distance = (self.position - other.position).magnitude
        return actual_distance <= min_distance
        
    def contains_point(self, point):
        if not isinstance(Vector, point):
            point = Vector(*point)
        min_distance = self.radius
        actual_distance = (self.position - point.position).magnitude
        return actual_distance <= min_distance
        
        
        