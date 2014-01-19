#!/usr/bin/python

from __future__ import division, absolute_import

import pygame

import time

Event = pygame.event.Event

def post(event_id, **attributes):
    e = Event(event_id, **attributes)
    pygame.event.post(e)
    
_events_cache = []
    
def post_delayed_event(event_id, delay, **attributes):
    global _events_cache
    e = Event(event_id, **attributes)
    _events_cache.append((time.time(), delay, e))

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
        self.handle_delayed_events()
        
        top = self.handlers['top']
        
        if name not in self.handlers:
            self.handlers[name] = {}
        
        current = self.handlers[name]
        
        for event in pygame.event.get():                
            if event.type in top:
                for handler in top[event.type]:
                    handler(event)
            if event.type in current:
                for handler in current[event.type]:
                    handler(event)
                    
        return None
        
    def handle_delayed_events(self):
        global _events_cache
        output = []
        for start, delay, event in _events_cache:
            if time.time() - start >= delay:
                pygame.event.post(event)
            else:
                output.append((start, delay, event))
        _events_cache = output
        