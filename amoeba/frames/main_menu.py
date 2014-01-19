#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import pygame

import events
import consts


class Button(object):
    def __init__(self, position, size, text, action):
        self.position = position
        self.size = size
        self.text = text
        self.action = action
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
            
    def is_within(self, coordinates):
        x, y, width, height = self.normalize()
        
        within_x = x < coordinates[0] < x + width
        within_y = y < coordinates[1] < y + height
        
        return within_x and within_y
        
        
        

class MainMenuFrame(object):
    def __init__(self):
        self.name = 'main_menu'
        self.title_font = pygame.font.SysFont('Segoe UI', 72)
        self.title_surface = self.title_font.render("A M O E B A", True, (255, 255, 255))
        
        self.start_button = Button(
            (consts.SCREEN_SIZE[0]/2, 250), 
            (400, 50), 
            "START", 
            lambda x: x)
            
        self.levels_button = Button(
            (consts.SCREEN_SIZE[0]/2, 350), 
            (400, 50), 
            "LEVEL SELECT", 
            lambda x: x)
            
        self.options_button = Button(
            (consts.SCREEN_SIZE[0]/2, 450), 
            (400, 50), 
            "OPTIONS", 
            lambda x: x)
            
    def start(self, events_manager):
        self.events_manager = events_manager
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.start_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.levels_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.options_button)
        
    def update(self):
        pass
        
    def draw(self, screen):
        screen.fill((0,0,0))
        
        self._draw_title(screen)
        self.start_button.render(screen)
        self.levels_button.render(screen)
        self.options_button.render(screen)
        
    def _draw_title(self, screen):
        width, height = self.title_surface.get_size()
        x, y = consts.SCREEN_SIZE[0] / 2 - width/2, 50
        screen.blit(self.title_surface, (x, y))
        
    def end():
        pass
        
        