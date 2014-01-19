#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import random
import math

import entity

def find_closest_target(entity, entities):
    targets = entities.get('user_controllable')
        
    closest_distance = float('inf')
    closest = None
    
    for target in targets:
        distance = (target.circles.centroid - entity.circles.centroid).magnitude
        if distance < closest_distance:
            closest_distance = distance
            closest = target
            
    return (closest.circles.centroid - entity.circles.centroid).angle

class DriftMovement(object):
    name = 'movement_ai'
    def __init__(self, speed):
        self.start = time.time()
        self.speed = speed
    
    def process(self, entity, entities):
        current = time.time()
        if current - self.start > 2:
            self.start = current
            for circle in entity.circles:
                circle.velocity.angle += random.uniform(-math.pi/8, math.pi/8)
                circle.velocity.magnitude = self.speed
    
class ChasingMovement(object):
    name = 'movement_ai'
    
    def __init__(self, speed):
        self.start = time.time()
        self.speed = speed
        
    def process(self, entity, entities):
        current = time.time()
        if current - self.start > 2:
            angle = find_closest(entity, entities).angle
            self.start = current
            for circle in entity.circles:
                circle.velocity.angle = angle
                circle.velocity.magnitude = self.speed
                
class FireSingleBullet(object):
    name = 'attack_ai'
    
    def __init__(self, rate):
        self.start = time.time()
        self.rate = rate
        
    def process(self, entity, entities):
        current = time.time()
        if current - self.start > 2:
            angle = find_closest(entity, entities).angle
            self.start = current
            
            #entities.add(entity.Bullet, 
    
    
    
    
                
                
                
                
        