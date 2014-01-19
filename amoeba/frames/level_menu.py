#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import pygame

import levels
import events
import consts

from frames.utils import *

class LevelSelectFrame(object):
    def __init__(self):
        self.name = 'level_select'
        self.title_font = pygame.font.SysFont('Segoe UI', 72)
        self.title_surface = self.title_font.render("L E V E L   S E L E C T", True, (255, 255, 255))
        
        self.buttons = []
        
        margin = consts.SCREEN_SIZE[0] - 150 * (4 + 1)
        for x in range(1, 5):
            for y in range(0, 2):
                self.buttons.append(Button(
                    (margin / 2 + 150 * x, 275 + y * 150), 
                    (100, 100),
                    str(x + 4 * y),
                    'game',
                    levels.level_map[x + 4 * y]))
            
    def start(self, events_manager):
        self.events_manager = events_manager
        
        for button in self.buttons:        
            self.events_manager.attach(
                self.name, pygame.MOUSEMOTION, button)
            self.events_manager.attach(
                self.name, pygame.MOUSEBUTTONDOWN, button)
        
    def update(self):
        pass
        
    def draw(self, screen):
        screen.fill((0,0,0))
        
        self._draw_title(screen)
        
        for button in self.buttons:
            button.render(screen)
        
    def suspend(self):
        pass
        
    def end(self):
        pass
        
    def _draw_title(self, screen):
        width, height = self.title_surface.get_size()
        x, y = consts.SCREEN_SIZE[0] / 2 - width/2, 50
        screen.blit(self.title_surface, (x, y))
        
        