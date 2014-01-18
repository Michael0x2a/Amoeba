#!/usr/bin/env python

import pygame

import events

def test(event):
    if event.key == pygame.K_DOWN:
        print 'Test!'
