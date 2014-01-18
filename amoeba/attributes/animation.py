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
        pygame.draw.circle(surface, entity.color.rgb, entity.position.pos, int(entity.radius))