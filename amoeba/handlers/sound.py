#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import consts
import events

from utils.vector import *

class SoundEffect(object):
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)
        self.effect = pygame.mixer.Channel(1)
        self.effect.set_volume(1.0)
        
    def __call__(self, event):
        self.effect.play(self.sound)
    