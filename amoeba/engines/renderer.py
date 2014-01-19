#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame
import math

import consts
from utils.vector import *


class Renderer(object):
    def __init__(self, entity_manager):
        self.entity_manager = entity_manager
        self.offset = 0.0

    def render(self, screen):
        self.clear_screen(screen)
        self.draw_cyclone(screen)
        self.draw_entities(screen)

    def clear_screen(self, screen):
        screen.fill((0,0,0))
        
    def draw_cyclone(self, screen):
        width, height = consts.SCREEN_SIZE
        mid_x, mid_y = int(width / 2), int(height / 2)
        
        mid = Cartesian(mid_x, mid_y)
        distance = math.sqrt(mid_x**2 + mid_y**2) + 30
        
        self.offset += 0.001 % (2*math.pi)
        
        for i in range(0, 12, 2):
            theta1 = Polar(distance + 5, i * math.pi/6 + self.offset)
            theta2 = Polar(distance + 5, (i + 1) * math.pi/6 + self.offset)
            points = [(mid_x, mid_y), (mid + theta1).pos, (mid + theta2).pos]
            pygame.draw.polygon(screen, (20, 20, 20), points)

    def draw_entities(self, screen):
        for entity in self.entity_manager.get('animation','drawable'):
            entity.animation.draw(entity, screen)
        for entity in self.entity_manager.get('amoeba_physics'):
            entity.amoeba_physics.draw(entity, screen)
