#!/usr/bin/env python

from __future__ import division

import pygame
pygame.init()

import events
import consts

class FrameManager(object):
    def __init__(self, frame_map):
        self.frames = frame_map
        
    def run(self):
        self.events = events.EventsManager()
        self.events.register_handler('top', pygame.QUIT, self.quit)
        self.init_pygame()
        
        self.frames[-1].start(self.events, self.screen)
        while True:
            self.events.process()
            self.frames[-1].update()
            self.frames[-1].draw(self.screen)
        
    def init_pygame(self):
        self.screen = pygame.display.set_mode(consts.SCREEN_SIZE)
        
    def quit(self, event):
        pygame.quit()
        sys.exit()
        # Add saving
        