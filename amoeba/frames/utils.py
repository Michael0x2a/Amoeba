#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import pygame

import events
import consts

class Button(object):
    def __init__(self, position, size, text, next_frame, level=None):
        self.position = position
        self.size = size
        self.text = text
        self.next_frame = next_frame
        self.level = level
        self.font = pygame.font.SysFont('Segoe UI', 40)
        
        self.rect_color = 0
        
        self.highlight = 0
        self.highlight_delta = 0
        
    def normalize(self):
        width, height = self.size
        x, y = self.position[0] - width/2, self.position[1] - height/2
        return (x, y + 2, width, height)
        
    def render(self, screen):
        self._draw_rect(screen)
            
        surface = self.font.render(self.text, True, (255, 255, 255))
        
        width, height = surface.get_size()
        x, y = self.position[0] - width/2, self.position[1] - height/2
        
        screen.blit(surface, (x, y))
        
    def _draw_rect(self, screen):
        self.highlight += self.highlight_delta
        if self.highlight < 0:
            self.highlight = 0
        if self.highlight > 255:
            self.highlight = 255
        
        pygame.draw.rect(
            screen, 
            (self.highlight, self.highlight, self.highlight), 
            pygame.Rect(self.normalize()),
            2)
        
    def __call__(self, event):
        if event.type == pygame.MOUSEMOTION:
            if self.is_within(event.pos):
                self.highlight_delta = 1
            else:
                self.highlight_delta = -1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_within(event.pos):
                events.post(consts.CHANGE_FRAME, frame=self.next_frame, level=self.level)
            
    def is_within(self, coordinates):
        x, y, width, height = self.normalize()
        
        within_x = x < coordinates[0] < x + width
        within_y = y < coordinates[1] < y + height
        
        return within_x and within_y