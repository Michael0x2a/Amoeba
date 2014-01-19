#!/usr/bin/env python

from __future__ import division, absolute_import

import sys

import pygame
pygame.init()

import events
import consts

from frames.game import GameFrame
from frames.main_menu import MainMenuFrame
from frames.level_menu import LevelSelectFrame

class FrameManager(object):
    def __init__(self, frame_map, start):
        self.frames = frame_map
        self.stack = [self.frames[start]]
        
    def run(self):
        self.events = events.EventsManager()
        self.events.attach('top', pygame.QUIT, self.quit)
        self.init_pygame()
        
        pygame.mixer.music.load('amoeba/assets/music_tracks/Voice of the Storm - The Enigma TNG.mp3')
        pygame.mixer.music.play(-1)
        
        self._adjust_music_volume()
        
        self.stack[-1].start(self.events)
        while True:
            next_frame, next_level = self.events.process(self.stack[-1].name)
            
            if next_frame is not None:
                # Any time a new frame is placed
                self._adjust_music_volume()
                
            if next_frame == 'destroy':
                while len(self.stack > 1):
                    frame = self.stack.pop()
                    state = frame.suspend()
                    frame.end()
                self.stack[-1].resume()
            elif next_frame == 'pop':
                frame = self.stack.pop()
                state = frame.suspend()
                frame.end()
                self.stack[-1].resume()
            elif next_frame is not None:
                self.stack[-1].suspend()
                self.stack.append(self.frames[next_frame])
                if next_level is not None:
                    self.stack[-1].start(self.events, next_level)
                else:
                    self.stack[-1].start(self.events)
                
            self.stack[-1].update()
            self.stack[-1].draw(self.screen)
            pygame.display.flip()
            
    def _adjust_music_volume(self):
        if self.stack[-1].name == 'game':
            pygame.mixer.music.set_volume(1) # full volume
        else:
            pygame.mixer.music.set_volume(0.5) # half volume
        
    def init_pygame(self):
        self.screen = pygame.display.set_mode(consts.SCREEN_SIZE)
        
    def quit(self, event):
        pygame.quit()
        sys.exit()
        # Add saving
        