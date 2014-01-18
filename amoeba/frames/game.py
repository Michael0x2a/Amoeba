#!/usr/bin/env python

from __future__ import division, absolute_import

import pygame
import events
import handlers
import entity
from utils.vector import *
from utils.circle import *

import engines

class GameFrame(object):
    def __init__(self):
        self.name = 'game'
        
    def start(self, events_manager):
        self.events_manager = events_manager
        self.events_manager.attach(self.name, pygame.KEYDOWN, handlers.test)
        
        # TODO: Make a level loading thing
        self.entities = entity.EntityManager(
            entity.Player(Circle(Cartesian(50, 50), Cartesian(0, 0), 20)))
            
        self.physics_engine = engines.physics.PhysicsEngine(self.entities, 1)
        self.rendering_engine = engines.renderer.Renderer(self.entities)
        
    def update(self):
        self.physics_engine.process()
        
    def draw(self, screen):
        self.rendering_engine.render(screen)
        
    def end():
        pass
        