#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import events

def test(event):
    if event.key == pygame.K_DOWN:
        print 'Test!'