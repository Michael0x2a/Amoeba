#!/usr/bin/env python

import pygame
import events
import handlers

class GameFrame(object):
    def __init__(self):
        self.name = 'game'
        
    def start(self, events_manager):
        self.events_manager = events_manager
        self.events_manager.attach(self.name, pygame.KEYDOWN, handlers.test)
        
    def update(self):
        pass
        
    def draw(self, screen):
        pass
        
    def end():
        pass
        