#!/usr/bin/env python

from __future__ import division

import pygame

import events

class FrameManager(object):
    def __init__(self, frame_map):
        self.frames = frame_map
        
    def run(self):
        self.events = events.EventsManager
        self.init_pygame()