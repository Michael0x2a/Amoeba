#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import events

from handlers.game import *
import handlers.sound as sound

def test(event):
    if event.key == pygame.K_DOWN:
        print 'Test!'
        if not hasattr(event, 'done'):
            events.post_delayed_event(pygame.KEYDOWN, 3, key=pygame.K_DOWN, done=True)
        