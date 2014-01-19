#!/usr/bin/env python

from __future__ import division, absolute_import

import time
import pygame

import events
import consts
import levels

from frames.utils import *


class MainMenuFrame(object):
    def __init__(self):
        self.name = 'main_menu'
        self.title_font = pygame.font.SysFont('Segoe UI', 72)
        self.title_surface = self.title_font.render("A M O E B A", True, (255, 255, 255))
        
        self.start_button = Button(
            (consts.SCREEN_SIZE[0]/2, 250), 
            (400, 60), 
            "START", 
            "game", levels.level_1)
            
        self.levels_button = Button(
            (consts.SCREEN_SIZE[0]/2, 350), 
            (400, 60), 
            "LEVEL SELECT", 
            "level_select")
            
        self.options_button = Button(
            (consts.SCREEN_SIZE[0]/2, 450), 
            (400, 60), 
            "OPTIONS", 
            "options")
            
    def start(self, events_manager):
        self.events_manager = events_manager
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.start_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.levels_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEMOTION, self.options_button)
            
        self.events_manager.attach(
            self.name, pygame.MOUSEBUTTONDOWN, self.start_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEBUTTONDOWN, self.levels_button)
        self.events_manager.attach(
            self.name, pygame.MOUSEBUTTONDOWN, self.options_button)
        
    def update(self):
        pass
        
    def draw(self, screen):
        screen.fill((0,0,0))
        
        self._draw_title(screen)
        self.start_button.render(screen)
        self.levels_button.render(screen)
        self.options_button.render(screen)
        
    def suspend(self):
        pass
        
    def end(self):
        pass
        
    def _draw_title(self, screen):
        width, height = self.title_surface.get_size()
        x, y = consts.SCREEN_SIZE[0] / 2 - width/2, 50
        screen.blit(self.title_surface, (x, y))
        
        