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

class GameFrame(object):
    def __init__(self):
        self.name = 'game'
        
    def start(self, events_manager, level):
        self.entities = entity.EntityManager()
        self.events_manager = events_manager
        
        level(self.name, self.entities, self.events_manager)
        
        
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
        