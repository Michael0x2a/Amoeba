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
            #scale = lambda scalar, current: int((current/circle.radius) * scalar)
            #for i in xrange(2, int(circle.radius), 2):
            #    r, g, b = color
            #    r, g, b = scale(r, i), scale(g, i), scale(b, i)
            #    pygame.draw.circle(surface, (r, g, b), circle.position.pos, i, 2)
            
class DisplayText(object):
    name = 'animation'
    
    def __init__(self, text, font='Segoi UI', size=30):
        self.font = pygame.font.SysFont(font, size)
        self.text = text
        self.surface = self.font.render(self.text, True, (200, 200, 200))
        
    def draw(self, entity, surface):
        width, height = self.surface.get_size()
        x, y = entity.position.pos
        
        x = int(x - width/2)
        y = int(y - height/2)
        
        x = x if x > 0 else 0
        y = y if y > 0 else 0
        surface.blit(self.surface, (x, y))
        
        
        
        
        