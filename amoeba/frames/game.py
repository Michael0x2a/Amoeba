#!/usr/bin/env python

from __future__ import division, absolute_import

import math

import pygame
import events
import handlers
import entity
import consts
from utils.vector import *
from utils.circle import *

import engines
import attributes

SPRINGS = [
    [None      , (0.001, 30.0), (0.001, 30.0), (0.001, 30.0)],
    [(0.001, 30.0), None, None, None],
    [(0.001, 30.0), None, None, None],
    [(0.001, 30.0), None, None, None]
]

class GameFrame(object):
    def __init__(self):
        self.name = 'game'
        
    def start(self, events_manager):
        # Construct entities
    
        # TODO: Make a level loading thing
        enemy1 = entity.InstakillEnemy(Circle(Cartesian(400, 400), Cartesian(0, 0), 30))
        '''player = entity.Player(
            SPRINGS,
            Circle(Cartesian(100, 100), Cartesian(0, 0), 30),
            Circle(Cartesian(50, 50), Cartesian(0, 0), 30),
            Circle(Cartesian(200, 50), Cartesian(0, 0), 30),
            Circle(Cartesian(100, 200), Cartesian(0, 0), 30)
            )'''
        player = entity.Player(SPRINGS, Circle(Cartesian(100, 100), Cartesian(0, 0), 30))
        
        drift = entity.Drifter(Circle(Cartesian(300, 50), Polar(1, 0), 5))
        test_powerup = entity.Powerup(
            Circle(Vector(50, 300), Vector(0, 0), 5), 
            attributes.SizeIncreasePowerup(30))
        text = entity.Text(Vector(50, 200), "Hello world")
        
        self.entities = entity.EntityManager(player, enemy1, drift, test_powerup, text)
        
        # Handlers
        
        self.events_manager = events_manager
        self.events_manager.attach(self.name, pygame.KEYDOWN, handlers.test)
        
        fling = handlers.Fling(player)
        self.events_manager.attach(self.name, pygame.MOUSEBUTTONDOWN, fling)
        self.events_manager.attach(self.name, pygame.MOUSEBUTTONUP, fling)
        
        self.events_manager.attach(self.name, consts.COLLIDE_EVENT, handlers.handle_collision)
        
        self.events_manager.attach(self.name, consts.REMOVE_POWERUP, handlers.handle_removed_powerups)
        
        self.events_manager.attach(self.name, consts.HEALTH_CHANGED, handlers.handle_health_changed)
        
        # Engines
        
        
        self.ai_engine = engines.ai.AIEngine(self.entities)
        self.physics_engine = engines.physics.PhysicsEngine(self.entities, 1)
        self.rendering_engine = engines.renderer.Renderer(self.entities)
        
    def update(self):
        self.entities.prune()
        self.ai_engine.process()
        self.physics_engine.process()
        
    def draw(self, screen):
        self.rendering_engine.render(screen)
        
    def suspend(self):
        return {}
        
    def end():
        pass
        