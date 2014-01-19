#!/usr/bin/env python

from __future__ import division, absolute_import

import math

class Vector(object):
    '''An object to represent either a change in position, or 
    just position (depending on context)'''
    def __init__(self, x, y):
        self.x = x
        self.y = y
            
    @property
    def magnitude(self):
        '''Sets the magnitude of the vector.'''
        return math.sqrt(self.x**2 + self.y**2)
        
    @magnitude.setter
    def magnitude(self, magnitude):
        '''Returns the magnitude of the vector, altering 
        x and y in the process, but keeping angle the same.'''
        angle = self.angle
        self.x = math.cos(angle) * magnitude
        self.y = math.sin(angle) * magnitude
        
    @property
    def angle(self):
        '''Returns the angle of the vector in radians, starting
        from the right-most axis and moving counter-lockwise.'''
        return math.atan2(self.y, self.x)
        
    @angle.setter
    def angle(self, angle):
        '''Sets the angle, altering x and y in the process,
        but keeping angle the same.'''
        magnitude = self.magnitude
        self.x = math.cos(angle) * magnitude
        self.y = math.sin(angle) * magnitude
        
    @property
    def pos(self):
        '''Gets the x and y coords of the vector, but converted 
        to ints for integration with pygame.'''
        return (int(self.x), int(self.y))
        
    def copy(self):
        '''Returns a complete copy of the vector.'''
        return Vector(self.x, self.y)
        
    def dot(self, other):
        '''Returns the dot product of two vectors.'''
        return self.x * other.x + self.y * other.y
        
    def cross(self, other):
        '''Returns the magnitude of the cross product of two vectors.'''
        return self.x * other.y - self.y - other.x
        
    def distance(self, other):
        '''Returns the distance between two vectors as a scalar'''
        return (self - other).magnitude

    def direction(self, other):
        '''Returns the direction from this vector to the other'''
        return (other - self).angle
        
    def normalize(self, value=1):
        return Polar(value, self.angle)
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
        
    def __div__(self, num):
        return Vector(self.x / num, self.y / num)
        
    def __truediv__(self, num):
        return Vector(self.x / num, self.y / num)
    
    def __mul__(self, num):
        return Vector(self.x * num, self.y * num)
        
    def __rmul__(self, num):
        return self.__mul__(num)
        
    def __neg__(self):
        return Polar(-self.magnitude, self.angle)
        
    def __repr__(self):
        return 'Vector({0}, {1})'.format(self.x, self.y)
        
def Cartesian(x, y):
    return Vector(x, y)
    
def Polar(magnitude, angle):
    v = Vector(0, 0)
    v.magnitude = magnitude
    v.angle = angle
    return v