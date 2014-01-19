#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

from utils.palette import *

class Drawable(object):
    name = 'drawable'
    
class Size(float):
    name = 'size'
    
class Color(RGB):
    name = 'color'
    
class CircleAnimation(object):
    name = 'animation'
    
    def draw(self, entity, surface):
        if 'health' in entity and entity.health <= 0:
            self._draw_circles(surface, entity, (80, 80, 80))
        else:
            self._draw_circles(surface, entity, entity.color.rgb)
                
    def _draw_circles(self, surface, entity, color):
        for circle in entity.circles:
                pygame.draw.circle(surface, color, circle.position.pos, int(circle.radius))