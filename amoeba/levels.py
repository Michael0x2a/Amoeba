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
        
def sound_effect_attachments(name, events):
    events.attach(
        name,
        consts.OBJECT_FLUNG,
        handlers.sound.SoundEffect(r'amoeba/assets/sound_effects/acid-burning.mp3'))

def level_1(name, entities, events):
    player = entity.Player(
        [
            [None]
        ],
        Circle(Cartesian(100, 100), Cartesian(0, 0), 15))
    for i in xrange(5):
        player.amoeba_physics.add_random_circle(player)
    # player.amoeba_physics.remove(3, player)
        
    entities.add(
        player,
        entity.TriggerRegion(
            Circle(Cartesian(100, 100), Cartesian(0, 0), 100),
            "trigger1"),
        entity.TriggerRegion(
            Circle(Cartesian(400, 100), Cartesian(0, 0), 100),
            "trigger2"),
        entity.TriggerRegion(
            Circle(Cartesian(700, 100), Cartesian(0, 0), 100),
            "trigger3"),
        entity.TriggerRegion(
            Circle(Cartesian(700, 500), Cartesian(0, 0), 100),
            "trigger4"),
        entity.TriggerRegion(
            Circle(Cartesian(400, 450), Cartesian(0, 0), 150),
            "trigger5"),
        entity.Food(
            Circle(Cartesian(700, 100), Cartesian(0, 0), 10),
            30),
        entity.Food(
            Circle(Cartesian(700, 100), Cartesian(0, 0), 10),
            30),
        entity.StationaryEnemy(
            SPRINGS,
            Circle(Cartesian(500, 500), Cartesian(0, 0), 15)),
        # entity.StationaryEnemy(
        #     Circle(Cartesian(400, 400), Cartesian(0, 0), 15)),
        # entity.StationaryEnemy(
        #     Circle(Cartesian(400, 500), Cartesian(0, 0), 15)),
        # entity.StationaryEnemy(
        #     Circle(Cartesian(250, 450), Cartesian(0, 0), 50)),
        entity.Food(
            Circle(Cartesian(400, 450), Cartesian(0, 0), 15),
            30)
    )
    
    standard_attachments(name, events, player)
    sound_effect_attachments(name, events)
    
    events.attach(
        name,
        consts.TRIGGER,
        handlers.RevealText(
            {
                'trigger1': ("Click and drag left", Cartesian(100, 200)),
                'trigger2': ("Movement requires sacrifice", Cartesian(400, 200)),
                'trigger3': ("Eat to recover", Cartesian(700, 200)),
                'trigger4': ("Bigger things are more dangerous", Cartesian(600, 400))
            },
            entities)
    )
        
        
        
def level_8(name, entities, events):
    
    '''entity.Player(
        SPRINGS,
        Circle(Cartesian(100, 100), Cartesian(0, 0), 30),
        Circle(Cartesian(50, 50), Cartesian(0, 0), 30),
        Circle(Cartesian(200, 50), Cartesian(0, 0), 30),
        Circle(Cartesian(100, 200), Cartesian(0, 0), 30)),'''
        
    player = entity.Player(
            SPRINGS, 
            Circle(Cartesian(100, 100), Cartesian(0, 0), 15),
            Circle(Cartesian(100, 150), Cartesian(0, 0), 15),
            Circle(Cartesian(150, 100), Cartesian(0, 0), 15),
            Circle(Cartesian(150, 150), Cartesian(0, 0), 15))
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
    sound_effect_attachments(name, events)
    

level_map = {
    1: level_1,
    2: level_1,
    3: level_1,
    4: level_1,
    5: level_1,
    6: level_1,
    7: level_1,
    8: level_8
}
    