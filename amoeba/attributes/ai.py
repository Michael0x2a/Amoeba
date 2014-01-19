#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import random
import math

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
        