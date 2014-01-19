#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

SCREEN_SIZE = (800, 600)

# EVENTS

COLLIDE_EVENT = pygame.USEREVENT + 1
REMOVE_POWERUP = pygame.USEREVENT + 2
HEALTH_CHANGED = pygame.USEREVENT + 3
ENTITY_DEATH = pygame.USEREVENT + 4
CHANGE_FRAME = pygame.USEREVENT + 5