#!/usr/bin/env python

from __future__ import division

import sys

import pygame
pygame.init()

import events
import consts

from frames.game import GameFrame

class FrameManager(object):
    def __init__(self, frame_stack):
        self.frames = frame_stack
        
    def run(self):
        self.events = events.EventsManager()
        self.events.attach('top', pygame.QUIT, self.quit)
        self.init_pygame()
        
        self.frames[-1].start(self.events)
        while True:
            self.events.process(self.frames[-1].name)
            self.frames[-1].update()
            self.frames[-1].draw(self.screen)
            pygame.display.flip()
        
    def init_pygame(self):
        self.screen = pygame.display.set_mode(consts.SCREEN_SIZE)
        
    def quit(self, event):
        pygame.quit()
        sys.exit()
        # Add saving
        