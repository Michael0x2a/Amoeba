#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import utils.color

class Drawable(object):
    name = 'drawable'
    
class Size(float):
    name = 'size'
    
class Color(utils.color.Color):
    name = 'color'
    
class CircleAnimation(object):
    name = 'animation'
    
    def draw(self, entity, surface):
        pygame.circle(surface, entity.color, entity.position.pos, int(entity.size))