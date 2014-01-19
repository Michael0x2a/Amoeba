#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

SCREEN_SIZE = (1000, 600)

# EVENTS

COLLIDE_EVENT = pygame.USEREVENT + 1
REMOVE_POWERUP = pygame.USEREVENT + 2
HEALTH_CHANGED = pygame.USEREVENT + 3
ENTITY_DEATH = pygame.USEREVENT + 4
CHANGE_FRAME = pygame.USEREVENT + 5
OBJECT_FLUNG = pygame.USEREVENT + 6
TRIGGER = pygame.USEREVENT + 7