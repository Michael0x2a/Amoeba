#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame

import entity
import handlers
import consts
import attributes

from utils.vector import *
from utils.circle import *


SPRINGS = [
    [None      , (0.001, 30.0), (0.001, 30.0), (0.001, 30.0)],
    [(0.001, 30.0), None, None, None],
    [(0.001, 30.0), None, None, None],
    [(0.001, 30.0), None, None, None]
]

def standard_attachments(name, events, player):
    events.attach(
        name, 
        pygame.KEYDOWN, 
        handlers.test)
    
    fling = handlers.Fling(player)
    events.attach(
        name, 
        pygame.MOUSEBUTTONDOWN, 
        fling)
    events.attach(
        name, 
        pygame.MOUSEBUTTONUP, 
        fling)
    
    events.attach(
        name, 
        consts.COLLIDE_EVENT, 
        handlers.handle_collision)
    
    events.attach(
        name, 
        consts.REMOVE_POWERUP, 
        handlers.handle_removed_powerups)
    
    events.attach(
        name, 
        consts.HEALTH_CHANGED, 
        handlers.handle_health_changed)

def level_1(name, entities, events):
    
    '''entity.Player(
        SPRINGS,
        Circle(Cartesian(100, 100), Cartesian(0, 0), 30),
        Circle(Cartesian(50, 50), Cartesian(0, 0), 30),
        Circle(Cartesian(200, 50), Cartesian(0, 0), 30),
        Circle(Cartesian(100, 200), Cartesian(0, 0), 30)),'''
        
    player = entity.Player(
            SPRINGS, 
            Circle(Cartesian(100, 100), Cartesian(0, 0), 30))
    # Entities
    entities.add(
        player,
        entity.InstakillEnemy(
            Circle(Cartesian(400, 400), Cartesian(0, 0), 30)),
        entity.Drifter(
            Circle(Cartesian(300, 50), Polar(1, 0), 5)),
        entity.Powerup(
            Circle(Vector(50, 300), Vector(0, 0), 5), 
            attributes.SizeIncreasePowerup(30)),
        entity.Text(
            Vector(50, 200), 
            "Hello world")
    )
    
    # Handlers
    standard_attachments(name, events, player)
    

level_map = {
    1: level_1,
    2: level_1,
    3: level_1,
    4: level_1,
    5: level_1,
    6: level_1,
    7: level_1,
    8: level_1
}
    