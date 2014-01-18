#!/usr/bin/python

from __future__ import division, absolute_import

import pygame

Event = pygame.event.Event

def post(event_id, **attributes):
    e = Event(event_id, **attributes)
    pygame.event.post(e)

class EventsManager(object):
    def __init__(self):
        self.handlers = {}
        self.user_events = []
        
    def attach(self, frame_name, event_id, handler):
        if frame_name not in self.handlers:
            self.handlers[frame_name] = {}
        if event_id not in self.handlers[frame_name]:
            self.handlers[frame_name][event_id] = []
        self.handlers[frame_name][event_id].append(handler)
        
    def process(self, name):
        top = self.handlers['top']
        current = self.handlers[name]
        
        for event in pygame.event.get():                
            if event.type in top:
                for handler in top[event.type]:
                    handler(event)
            if event.type in current:
                for handler in current[event.type]:
                    handler(event)